Das ist mein Python playground.
Sammlung von Tutorials und kleinen Projekten.

## Overview

Projekte sind unter `/Projekte` und Python Basics in `/basic_details` zu finden

___

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

**Update von uv**
```bash
uv self update
# oder
pip install --upgrade uv
```

### uv Workflow 1: Projekt komplett neu aufsetzen

#### 1. Projekt initialisieren
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

#### 2. Virtuelle Umgebung aktivieren
```bash
uv venv
```

(Optional: Wenn die gewünschte Python-Version noch nicht installiert ist.)
```bash
uv python list # zeigt alle verfügbaren Python-Versionen an
uv python install 3.12
```

Python-Versionen werden in `~/.uv/python/` installiert.   
Um eine Python-Version zu deinstallieren:
```bash
uv python uninstall <version>
# z.B. uv python uninstall 3.12 
```

#### 3. Projektabhängigkeiten installieren / löschen
```bash
uv add <package-name>
# z.B. uv add requests

# Oder entfernen
uv remove <package-name>
```
Alle Abhängigkeiten werden mit `uv add` und `uv remove` in `uv.lock` automatisch gespeichert.   
Fügt man eine Abhängigkeit manuell in `pyproject.toml` hinzu, muss man sie anschließend mit `uv sync` installieren und mit `uv lock` aktualisieren:    
```bash
uv sync
uv lock
```

Um alle Abhängigkeiten anzuzeigen:
```bash
uv tree
```

#### 4. Projekt ausführen
```bash
uv run python <script-name>
# z.B. uv run python main.py

# Oder Modul ausführen
uv run -m <module-name>
# z.B. uv run -m hund.main

# Mit Parameter
uv run python <script-name> <parameter>
# z.B. uv run python main.py --help -I <parameter>
```

#### 5. Tests ausführen

Alle Tests ausführen:   
```bash
uv run pytest
```

Einzelne Test-Datei ausführen:
```bash
uv run pytest <test-file-name>
# z.B. uv run pytest test/test_main.py
```

`-v` für verbose / ausführlicher output:
```bash
uv run pytest -v
```

Einzelner Test oder Klasse einer Test-Datei ausführen:
```bash
uv run pytest <test-file-name>::<test-function-name>
# z.B. uv run pytest test/test_main.py::test_addition
# z.B. uv run pytest test/test_main.py::TestClassName 
```

#### 6. Code prüfen und formatieren
```bash
# ruff installieren
uv add --dev ruff

# Code prüfen und formatieren
uv run ruff check .
uv run ruff format .
```

#### 7. Git commit und push
`uv.lock` und `pyproject.toml` werden automatisch aktualisiert, wenn `uv add/remove` ausgeführt wird.      
Diese Dateien sollten daher immer mit in das Git Repository aufgenommen werden.

```bash
git add uv.lock pyproject.toml
git commit -m "Update dependencies"
git push
```
___

### uv Workflow 2: Bestehendes Projekt aus Git klonen

#### 1. Repository klonen
```bash
git clone <repository-url>
cd <repository-name>
```

#### 2. Optional: Python-Version installieren (uv erkennt die gewünschte Version aus `.python-version` oder `pyproject.toml`)
```bash
uv python list # zeigt alle verfügbaren Python-Versionen an
uv python install <version>
# z.B. uv python install 3.12
```

#### 3. Abhängigkeiten installieren
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

___

## Anwendung bauen und publishen

#### build

```bash
uv build
```
Einen Build braucht man, wenn:   
- prüfen möchte, ob ein Paket korrekt gebaut werden kann
- die erzeugten Dateien lokal testen möchte
- sie später hochladen möchte

-> erstellt installierbare Python-Pakete   
Es ensteht ein Verzeichnis `dist/` mit den Dateien:
```
dist/
├── meinprojekt-0.1.0-py3-none-any.whl
├── meinprojekt-0.1.0.tar.gz
```

#### publish
```bash
uv publish
```
mit publish lädt man die zuvor gebauten Dateien (uv build) in ein Paket-Repository hoch.  
z.B. auf [PyPI](https://pypi.org/) oder AWS Codeartifact Repository.  

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

