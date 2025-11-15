from notes_manager import add_note, list_notes, delete_note, search_notes


def show_menu():
    print("\n===================================")
    print("             NOTES APP             ")
    print("===================================")
    print("1) Add Note")
    print("2) List Notes")
    print("3) Delete Note")
    print("4) Search Notes")
    print("q) Quit")
    print("===================================")


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ").strip().lower()

        if choice == "1":
            add_note()
        elif choice == "2":
            list_notes()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            search_notes()
        elif choice == "q":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid option! Please try again.")


if __name__ == "__main__":
    main()
