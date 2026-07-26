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
            "The database already exists. If you'd like to overwrite it, you must delete it manually."
        )
