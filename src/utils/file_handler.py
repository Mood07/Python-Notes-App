import json
import os

DATA_FILE = "notes.json"


def load_notes():
    """Load notes from JSON file or return an empty list."""
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


def save_notes(notes):
    """Save notes to JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(notes, file, indent=4)
