from utils.file_handler import load_notes, save_notes


def add_note():
    notes = load_notes()
    title = input("Enter note title: ").strip()
    content = input("Enter note content: ").strip()

    if not title:
        print("Title cannot be empty!")
        return

    note = {"title": title, "content": content}
    notes.append(note)
    save_notes(notes)

    print("Note added successfully!")


def list_notes():
    notes = load_notes()

    if not notes:
        print("No notes found.")
        return

    print("\nYour Notes:")
    print("------------------------")
    for idx, note in enumerate(notes, 1):
        print(f"{idx}) {note['title']}")
    print("------------------------")


def delete_note():
    notes = load_notes()

    if not notes:
        print("No notes to delete.")
        return

    list_notes()

    try:
        index = int(input("Enter note number to delete: ")) - 1
        deleted = notes.pop(index)
        save_notes(notes)
        print(f"Deleted note: {deleted['title']}")
    except (ValueError, IndexError):
        print("Invalid note number!")


def search_notes():
    notes = load_notes()
    keyword = input("Enter keyword to search: ").strip().lower()

    results = [
        note for note in notes
        if keyword in note["title"].lower() or keyword in note["content"].lower()
    ]

    if not results:
        print("No matching notes found.")
        return

    print("\nSearch Results:")
    print("------------------------")
    for idx, note in enumerate(results, 1):
        print(f"{idx}) {note['title']}")
    print("------------------------")
