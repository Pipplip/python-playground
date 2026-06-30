Das ist mein Python playground.
Collection von Tutorials und kleinen Projekten.

## Overview

Projekte sind unter `/Projekte` und Python Basics in `/basic_details` zu finden

## uv   
all-in-one tool für Python Projekte:   
Es enthält:  
- pip (package manager)
- venv (virtual environment)
- pyproject.toml (project configuration file)

**Install uv**
```bash
pip install uv
```

### Workflow: Projekt komplett neu aufsetzen

1. Projekt initialisieren
```bash
uv init <project-name>
# z.B. uv init meinprojekt

cd meinprojekt
```

Init generiert folgendes:
```
meinprojekt/
│
├── .git
├── .gitignore
├── .python-version
├── README.md
├── pyproject.toml
└── src/
    └── meinprojekt/
        └── __init__.py
```

Beispiel `pyproject.toml`:
```toml
[project]
name = "my-project"
version = "0.1.0"
description = "A sample Python project"
readme = "README.md"
require-python = ">=3.12"
dependencies = [
    "requests>=2.31.0",
    "flask==2.3.3",
    "numpy>=1.24.0,<2.0.0"
]
```

2. Virtuelle Umgebung aktivieren
```bash
uv venv
```

(Optional: Wenn die gewünschte Python-Version noch nicht installiert ist.)
```bash
uv python install 3.12
```

3. Projektabhängigkeiten installieren / löschen
```bash
uv add <package-name>
# z.B. uv add requests

# Oder entfernen
uv remove <package-name>
```

4. Projekt ausführen
```bash
uv run python <script-name>
# z.B. uv run python main.py

# Oder Modul ausführen
uv run -m <module-name>
# z.B. uv run -m hund.main
```

5. Tests ausführen
```bash
uv run pytest
```

6. Code prüfen und formatieren
```bash
# ruff installieren
uv add --dev ruff

# Code prüfen und formatieren
uv run ruff check .
uv run ruff format .
```

7. Git commit und push
`uv.lock` und `pyproject.toml` werden automatisch aktualisiert, wenn `uv add/remove` ausgeführt wird.      
Diese Dateien sollten daher immer mit in das Git Repository aufgenommen werden.

```bash
git add uv.lock pyproject.toml
git commit -m "Update dependencies"
git push
```

### Workflow 2: Bestehendes Projekt aus Git klonen

1. Repository klonen
```bash
git clone <repository-url>
cd <repository-name>
```

2. Optional: Python-Version installieren (uv erkennt die gewünschte Version aus `.python-version` oder `pyproject.toml`)
```bash
uv python install <version>
# z.B. uv python install 3.12
```

3. Abhängigkeiten installieren
```bash
uv sync
```

Dabei wird automatisch:   
- die virtuelle Umgebung (.venv) erstellt (falls sie noch nicht existiert)
- alle Abhängigkeiten aus uv.lock installiert

Ein separater Aufruf von uv venv ist in der Regel nicht nötig, da uv sync dies übernimmt.


**Important commands:**   

| Command                | Description                                                                     |
|------------------------|---------------------------------------------------------------------------------|
| `uv init`              | Initialize a new project (generates pyproject.toml and src folder)              |
| `uv sync`              | Sync dependencies from pyproject.toml to the project environment (updates venv) |
| `uv update`            | Update installed packages                                                       |
| `uv run <script-name>` | Run a Python script within the project environment                              |
| `uv run -m hund.main`  | Runs a Python Module (src/hund/) with main class                                |
| `uv list`              | List installed dependencies in the project environment                          |


____    
## Execute python script (ohne uv)

```bash
python Basics-summary.py
```

## Execute module (ohne uv)
```bash
export PYTHONPATH="$PYTHONPATH:$(pwd)"
python -m <directoy>.<project-name>

# Bsp:
python -m TestPaket.a

```
__Info:__ ```__init__.py``` needs to be created in sub directories of each project if it is started as module.

