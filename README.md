This is my Python playground.
Collection of tutorials and small projects.

## Overview

Projects can be found in /Projekte and Python basics in more detail in /basic_details

## uv   
all-in-one modern tool for python projects:   
It includes:  
- pip (package manager)
- venv (virtual environment)
- pyproject.toml (project configuration file)

**Init**
```bash
uv init <project-name>
```
Init generates a project structure with a ```pyproject.toml``` file and a ```src``` directory.

Example `pyproject.toml`:
```toml
[project]
name = "my-project"
version = "0.1.0"
description = "A sample Python project"
dependencies = [
    "requests>=2.31.0",
    "flask==2.3.3",
    "numpy>=1.24.0,<2.0.0"
]
```

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
## Execute python script

```bash
python Basics-summary.py
```

## Execute module
```bash
export PYTHONPATH="$PYTHONPATH:$(pwd)"
python -m <directoy>.<project-name>

# Bsp:
python -m TestPaket.a

```
__Info:__ ```__init__.py``` needs to be created in sub directories of each project if it is started as module.

