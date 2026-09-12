import os
import json
from pathlib import Path


def initialize():
    db_path = Path(__file__).resolve().parent.parent / "db.json"

    try:
        with open(db_path, "x") as file:
            json.dump([{}], file, indent=4)
            print("Database created in the root folder.")
    except FileExistsError:
        print(
            "The database already exists. If you'd like to overwrite it, you must delete it with: db -rm"
        )

def remove():
    db_path = Path(__file__).resolve().parent.parent / "db.json"

    if os.path.exists(db_path):
        os.remove(db_path)
        print(f"File '{db_path}' deleted successfully.")
    else:
        print(f"File '{db_path}' not found.")


def generate_sample():
    sample = '''
[
  {
    "id": 0,
    "title": "Set up project directory",
    "description": "Create my_module subfolder and initialize __init__.py",
    "status": "completed",
    "priority": "high"
  },
  {
    "id": 1,
    "title": "Implement CLI parser",
    "description": "Use argparse to handle task creation and listing commands",
    "status": "in_progress",
    "priority": "high"
  },
  {
    "id": 2,
    "title": "Configure Ruff in Neovim",
    "description": "Ensure auto-formatting and __all__ sorting rule (RUF022) works on save",
    "status": "in_progress",
    "priority": "medium"
  },
  {
    "id": 3,
    "title": "Add data validation",
    "description": "Restrict task status options to pending, in_progress, and completed",
    "status": "pending",
    "priority": "low"
  }
]
'''
    with open("db.json", "w") as file:
        file.write(sample)