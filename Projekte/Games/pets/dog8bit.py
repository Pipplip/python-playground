"""8-bit pixel-art dog pet built with pygame.

Controls:
- W or Space: Walk
- S: Sit
- Z: Sleep
- Q or Escape: Quit

Movement improvements over v1:
- 24 FPS for smoother motion
- 4-frame walk cycle with a neutral mid-stride frame (WALK_0)
- Vertical body bob synchronized with each step
- Independent tail-wag animation (3 heights: up / mid / down)
- Acceleration when starting to walk, deceleration when stopping
- Brief turning pause at screen edges before reversing direction
- Slow tail-wag and gradual stop while sitting
- Eye-blink and staggered floating Zzz while sleeping
"""

from __future__ import annotations

import math
from typing import Final

import pygame
from pygame import Surface

# ─── Tuneable constants ───────────────────────────────────────────
PIXEL: Final[int] = 4           # virtual-pixel side length (px)
SCREEN_W: Final[int] = 640
SCREEN_H: Final[int] = 420
GROUND_Y: Final[int] = 340
FPS: Final[int] = 24            # higher FPS → smoother curves / bob
DOG_SPEED: Final[float] = 1.5   # cruising speed  (px / frame)
ACCEL: Final[float] = 0.18      # acceleration    (px / frame²)
DECEL: Final[float] = 0.25      # deceleration    (px / frame²)
BOB_AMP: Final[float] = 3.0     # vertical bob amplitude (real px)
TURN_PAUSE: Final[int] = 14     # frames to pause at wall before turning

# ─── Colors ───────────────────────────────────────────────────────
SKY: Final = (135, 206, 235)
SUN: Final = (255, 220, 64)
WHITE: Final = (255, 255, 255)
BLACK: Final = (0, 0, 0)
GROUND_G: Final = (56, 142, 60)
GROUND_D: Final = (33, 97, 52)
GRASS_BRIGHT: Final = (102, 187, 106)
ZZZ_COLOR: Final = (110, 110, 200)

PALETTE: Final[dict[str, tuple[int, int, int]]] = {
    "D": (92, 51, 23),
    "B": (160, 82, 45),
    "T": (210, 180, 140),
    "K": (20, 20, 20),
    "P": (240, 150, 130),
}

# ─── Sprite grids  (20 chars × 14 rows, '.' = transparent) ───────
# All walk/sit grids carry the tail at its "mid" position (row 3,
# cols 14-16 = DDD).  _with_tail() moves that DDD to row 2 ("up")
# or row 5 ("down") at sprite-build time.

# Neutral / mid-stride transition — legs close together
WALK_0: Final[tuple[str, ...]] = (
    "..DD................",
    ".DPPD...............",
    "DBBBD...............",
    "DBKBD..........DDD..",
    "DBBBDDDDDDDDDDDBBD..",
    ".DTTKBBBBBBBBBBD....",
    "..DDDBBBBBBBBBBD....",
    "....DTTTBBBBBBBD....",
    "....DDDDDDDDDDD.....",
    ".....DBD..DBD.......",
    ".....DBD..DBD.......",
    ".....DDD..DDD.......",
    "....................",
    "....................",
)

# Stride A — front leg forward, back leg back
WALK_1: Final[tuple[str, ...]] = (
    "..DD................",
    ".DPPD...............",
    "DBBBD...............",
    "DBKBD..........DDD..",
    "DBBBDDDDDDDDDDDBBD..",
    ".DTTKBBBBBBBBBBD....",
    "..DDDBBBBBBBBBBD....",
    "....DTTTBBBBBBBD....",
    "....DDDDDDDDDDD.....",
    ".....DBD....DBD.....",
    ".....DBD....DBD.....",
    ".....DDD....DDD.....",
    "....................",
    "....................",
)

# Stride B — front leg back, back leg forward
WALK_2: Final[tuple[str, ...]] = (
    "..DD................",
    ".DPPD...............",
    "DBBBD...............",
    "DBKBD..........DDD..",
    "DBBBDDDDDDDDDDDBBD..",
    ".DTTKBBBBBBBBBBD....",
    "..DDDBBBBBBBBBBD....",
    "....DTTTBBBBBBBD....",
    "....DDDDDDDDDDD.....",
    "......DBD..DBD......",
    "......DBD..DBD......",
    "......DDD..DDD......",
    "....................",
    "....................",
)

# Sitting — haunches down, front leg extended
SIT: Final[tuple[str, ...]] = (
    "..DD................",
    ".DPPD...............",
    "DBBBD...............",
    "DBKBD..........DDD..",   # tail tip restored so _with_tail works
    "DBBBDDDDDDDDDDDBBD..",
    ".DTTKBBBBBBBBBBD....",
    "..DDDBBBBBBBBBBD....",
    "....DTTTBBBBBBBD....",
    "....DDDDDDDDDDD.....",
    ".....DBD............",
    ".....DBD.DBBBBBD....",
    ".....DDD.DBBBBBD....",
    ".........DDDDDDD....",
    "....................",
)

# Sleeping — eyes open
SLEEP_1: Final[tuple[str, ...]] = (
    "....................",
    "....................",
    "....................",
    "..DD................",
    ".DPPD...............",
    "DBBBD.DDDDDDDDDDDDDD",
    "DBKBD.DBBBBBBBBBBBBD",
    "DTTTD.DBBBBBBBBBBBBD",
    ".DDDDDTTTBBBBBBBBBBD",
    "......DDDDDDDDDDDDDD",
    ".......DBD.....DBD..",
    ".......DDD.....DDD..",
    "....................",
    "....................",
)

# Sleeping — eyes closed (blink frame)
SLEEP_2: Final[tuple[str, ...]] = (
    "....................",
    "....................",
    "....................",
    "..DD................",
    ".DPPD...............",
    "DBBBD.DDDDDDDDDDDDDD",
    "DBDBD.DBBBBBBBBBBBBD",   # K → D = closed eye
    "DTTTD.DBBBBBBBBBBBBD",
    ".DDDDDTTTBBBBBBBBBBD",
    "......DDDDDDDDDDDDDD",
    ".......DBD.....DBD..",
    ".......DDD.....DDD..",
    "....................",
    "....................",
)


# ─── Tail-wag helper ──────────────────────────────────────────────

def _with_tail(grid: tuple[str, ...], pos: str) -> tuple[str, ...]:
    """Return *grid* with the tail tip relocated to *pos*.

    "up"   – tip at row 2, tail held high (excited wag)
    "mid"  – tip at row 3 (default, neutral)
    "down" – tip swept to row-5 level (horizontal/drooping)
    """
    if pos == "mid":
        return grid  # default position, nothing to change

    rows = [list(r) for r in grid]

    if pos == "up":
        # Lift tip from row 3 → row 2
        rows[3][14] = rows[3][15] = rows[3][16] = "."
        rows[2][14] = rows[2][15] = rows[2][16] = "D"

    elif pos == "down":
        # Remove tip from row 3, push it to the right of the body at row 5
        rows[3][14] = rows[3][15] = rows[3][16] = "."
        rows[5][15] = "B"
        rows[5][16] = "B"
        rows[5][17] = "D"

    return tuple("".join(r) for r in rows)


# ─── Sprite builder ───────────────────────────────────────────────

class State:
    WALK:  Final[str] = "Walk"
    SIT:   Final[str] = "Sit"
    SLEEP: Final[str] = "Sleep"


# sprites[direction][state][tail_pos] → list[Surface]
SpriteBank = dict[int, dict[str, dict[str, list[Surface]]]]

_TAIL_POSITIONS = ("up", "mid", "down")
_WALK_CYCLE = (WALK_0, WALK_1, WALK_0, WALK_2)  # 4-frame stride cycle


def _build_surface(grid: tuple[str, ...], flip: bool = False) -> Surface:
    w = len(grid[0]) * PIXEL
    h = len(grid) * PIXEL
    surf = pygame.Surface((w, h), pygame.SRCALPHA)
    for ry, row in enumerate(grid):
        for cx, ch in enumerate(row):
            color = PALETTE.get(ch)
            if color:
                pygame.draw.rect(surf, color, (cx * PIXEL, ry * PIXEL, PIXEL, PIXEL))
    return pygame.transform.flip(surf, True, False) if flip else surf


def build_sprites() -> SpriteBank:
    bank: SpriteBank = {}
    for direction in (1, -1):
        flip = direction == -1
        bank[direction] = {
            State.WALK: {
                t: [_build_surface(_with_tail(g, t), flip) for g in _WALK_CYCLE]
                for t in _TAIL_POSITIONS
            },
            State.SIT: {
                t: [_build_surface(_with_tail(SIT, t), flip)]
                for t in _TAIL_POSITIONS
            },
            State.SLEEP: {
                "mid": [_build_surface(SLEEP_1, flip), _build_surface(SLEEP_2, flip)]
            },
        }
    return bank


# ─── Dog entity ───────────────────────────────────────────────────

class Dog:
    # Leg-cycle: 4 frames × 3 ticks = 12 ticks total  →  0.5 s at 24 FPS
    _LEG_TICKS: Final[int] = 3
    _LEG_FRAMES: Final[int] = 4

    # Tail-wag timing (ticks between position steps)
    _TAIL_WALK_PERIOD:  Final[int] = 8   # fast wag while walking
    _TAIL_SIT_PERIOD:   Final[int] = 28  # slow, lazy wag while sitting

    # Sleep blink: open for N ticks, closed for M ticks
    _BLINK_OPEN:   Final[int] = 70
    _BLINK_CLOSED: Final[int] = 6

    def __init__(self, ground_y: int, sprites: SpriteBank) -> None:
        self.ground_y = ground_y
        self.sprites  = sprites
        self.state     = State.WALK
        self.direction = 1
        self.x         = 120.0
        self.velocity  = 0.0      # current horizontal speed (px/frame)

        self._leg_tick   = 0      # 0 … LEG_FRAMES*LEG_TICKS − 1
        self._tail_tick  = 0      # free-running counter for tail wag
        self._tail_idx   = 0      # index into _TAIL_POSITIONS  (0/1/2)
        self._blink_tick = 0      # free-running counter for eye blink
        self._zzz_tick   = 0
        self._turn_cd    = 0      # turn cooldown (counts down to 0)
        self._next_dir   = 1      # direction to adopt after cooldown

    # ── Public API ────────────────────────────────────────────────

    def set_state(self, state: str) -> None:
        if self.state == state:
            return
        self.state = state
        self._leg_tick  = 0
        self._zzz_tick  = 0
        self._blink_tick = 0

    def update(self) -> None:
        self._tail_tick += 1

        if self.state == State.WALK:
            self._update_walk()
        elif self.state == State.SIT:
            self._update_sit()
        elif self.state == State.SLEEP:
            self._update_sleep()

    def draw(self, screen: Surface, font: pygame.font.Font) -> None:
        sprite  = self._current_sprite()
        draw_x  = int(self.x)
        draw_y  = self.ground_y - sprite.get_height() + self._bob_offset
        screen.blit(sprite, (draw_x, draw_y))
        if self.state == State.SLEEP:
            self._draw_zzz(screen, font, draw_x, draw_y)

    # ── State-specific update logic ───────────────────────────────

    def _update_walk(self) -> None:
        # Always advance leg animation
        self._leg_tick = (self._leg_tick + 1) % (self._LEG_FRAMES * self._LEG_TICKS)

        # Tail wag: step through up → mid → down → mid → up …
        if self._tail_tick % self._TAIL_WALK_PERIOD == 0:
            # Sinusoidal mapping: 0→up, 1→mid, 2→down, 3→mid, …
            cycle = (self._tail_tick // self._TAIL_WALK_PERIOD) % 4
            self._tail_idx = [0, 1, 2, 1][cycle]

        # Turning cooldown: dog pauses before reversing
        if self._turn_cd > 0:
            self._turn_cd -= 1
            self.velocity = max(0.0, self.velocity - DECEL)
            if self._turn_cd == 0:
                self.direction = self._next_dir
            return  # no horizontal movement while turning

        # Accelerate up to cruising speed
        self.velocity = min(DOG_SPEED, self.velocity + ACCEL)
        self.x += self.velocity * self.direction

        # Wall collision → start turn cooldown
        sprite_w = self._current_sprite().get_width()
        margin   = 24.0
        if self.direction == 1 and self.x >= SCREEN_W - sprite_w - margin:
            self.x        = float(SCREEN_W - sprite_w - margin)
            self._turn_cd = TURN_PAUSE
            self._next_dir = -1
            self.velocity  = 0.0
        elif self.direction == -1 and self.x <= margin:
            self.x        = margin
            self._turn_cd = TURN_PAUSE
            self._next_dir = 1
            self.velocity  = 0.0

    def _update_sit(self) -> None:
        # Glide to a stop
        if self.velocity > 0:
            self.velocity = max(0.0, self.velocity - DECEL)
            self.x += self.velocity * self.direction

        # Slow tail wag while sitting
        if self._tail_tick % self._TAIL_SIT_PERIOD == 0:
            cycle = (self._tail_tick // self._TAIL_SIT_PERIOD) % 4
            self._tail_idx = [0, 1, 2, 1][cycle]

    def _update_sleep(self) -> None:
        # Glide to a stop
        if self.velocity > 0:
            self.velocity = max(0.0, self.velocity - DECEL)
            self.x += self.velocity * self.direction
        self._blink_tick += 1
        self._zzz_tick   += 1

    # ── Computed display helpers ──────────────────────────────────

    @property
    def _bob_offset(self) -> int:
        """Vertical body bob: rises at each foot-fall, sinks between steps."""
        if self.state != State.WALK or self._turn_cd > 0 or self.velocity < 0.4:
            return 0
        # Two bobs per full stride cycle
        phase = (self._leg_tick / (self._LEG_FRAMES * self._LEG_TICKS)) * 2 * math.pi
        return -round(abs(math.sin(phase * 2)) * BOB_AMP)

    @property
    def _tail_pos(self) -> str:
        return _TAIL_POSITIONS[self._tail_idx]

    def _current_sprite(self) -> Surface:
        state_bank = self.sprites[self.direction][self.state]

        if self.state == State.WALK:
            tail_frames = state_bank.get(self._tail_pos, state_bank["mid"])
            leg_frame   = self._leg_tick // self._LEG_TICKS
            return tail_frames[leg_frame % len(tail_frames)]

        if self.state == State.SIT:
            tail_frames = state_bank.get(self._tail_pos, state_bank["mid"])
            return tail_frames[0]

        # SLEEP — eye blink
        blink_cycle = (self._blink_tick % (self._BLINK_OPEN + self._BLINK_CLOSED))
        frame = 1 if blink_cycle >= self._BLINK_OPEN else 0
        return state_bank["mid"][frame]

    # ── Zzz drawing ───────────────────────────────────────────────

    def _draw_zzz(self, screen: Surface, font: pygame.font.Font,
                  dog_x: int, dog_y: int) -> None:
        """Staggered, floating Zzz letters that fade in and drift upward."""
        base_x = dog_x + 16
        base_y = dog_y - 4
        for i, letter in enumerate(("z", "Z", "Z")):
            # Each letter has its own phase offset so they appear sequentially
            t     = self._zzz_tick / 18.0 + i * 1.1
            rise  = ((self._zzz_tick + i * 22) * 0.8) % 52
            sway  = math.sin(t * 1.3) * 4
            alpha = max(40, min(255, int(160 + 90 * math.sin(t))))
            glyph = font.render(letter, False, ZZZ_COLOR)
            glyph.set_alpha(alpha)
            screen.blit(glyph, (base_x + i * 13 + sway, base_y - rise - i * 5))


# ─── Background ───────────────────────────────────────────────────

def draw_sun(screen: Surface) -> None:
    block   = 8
    start_x = SCREEN_W - 92
    start_y = 30
    for row in range(3):
        for col in range(3):
            pygame.draw.rect(screen, SUN,
                             (start_x + col * block, start_y + row * block, block, block))


def draw_cloud(screen: Surface, x: int, y: int) -> None:
    for bx, by, bw, bh in ((1, 0, 4, 1), (0, 1, 6, 1), (1, 2, 4, 1)):
        pygame.draw.rect(screen, WHITE, (x + bx * 8, y + by * 8, bw * 8, bh * 8))


def draw_ground(screen: Surface) -> None:
    pygame.draw.rect(screen, GROUND_D, (0, GROUND_Y, SCREEN_W, SCREEN_H - GROUND_Y))
    pygame.draw.rect(screen, GROUND_G, (0, GROUND_Y, SCREEN_W, 14))
    for x in range(0, SCREEN_W, 18):
        pygame.draw.rect(screen, GRASS_BRIGHT, (x + 2,  GROUND_Y - 6,  4, 6))
        pygame.draw.rect(screen, GRASS_BRIGHT, (x + 6,  GROUND_Y - 10, 4, 10))
        pygame.draw.rect(screen, GRASS_BRIGHT, (x + 10, GROUND_Y - 6,  4, 6))


def draw_background(screen: Surface) -> None:
    screen.fill(SKY)
    draw_sun(screen)
    for cloud_x, cloud_y in ((40, 48), (170, 78), (310, 42), (470, 92)):
        draw_cloud(screen, cloud_x, cloud_y)
    draw_ground(screen)


# ─── HUD ──────────────────────────────────────────────────────────

def draw_hud(screen: Surface, font: pygame.font.Font, state: str) -> None:
    text   = f"State: {state}   W/Space Walk   S Sit   Z Sleep   Q/Esc Quit"
    shadow = font.render(text, False, BLACK)
    label  = font.render(text, False, WHITE)
    text_y = SCREEN_H - 26
    screen.blit(shadow, (13, text_y + 1))
    screen.blit(label,  (12, text_y))


# ─── Entry point ──────────────────────────────────────────────────

def main() -> None:
    pygame.init()
    pygame.display.set_caption("8-Bit Dog Pet")
    screen   = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    clock    = pygame.time.Clock()
    hud_font = pygame.font.Font(None, 22)
    zzz_font = pygame.font.Font(None, 28)
    dog      = Dog(GROUND_Y, build_sprites())

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_q, pygame.K_ESCAPE):
                    running = False
                elif event.key == pygame.K_s:
                    dog.set_state(State.SIT)
                elif event.key == pygame.K_z:
                    dog.set_state(State.SLEEP)
                elif event.key in (pygame.K_w, pygame.K_SPACE):
                    dog.set_state(State.WALK)

        dog.update()
        draw_background(screen)
        dog.draw(screen, zzz_font)
        draw_hud(screen, hud_font, dog.state)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
