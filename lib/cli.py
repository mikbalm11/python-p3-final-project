# lib/cli.py

from helpers import (
    exit_program,
    trailname,
    hikername,
    hikename,
    list_hiker_hikes,
    add_trail,
    find_trail_by_id,
    find_trail_by_name
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_hiker_hikes()
        elif choice == "2":
            trailname()
        elif choice == "3":
            hikername()
        elif choice == "4":
            hikename()
        elif choice == "5":
            add_trail()
        elif choice == "6":
            find_trail_by_id()
        elif choice == "7":
            find_trail_by_name()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. List hiker's completed trails")
    print("1. Some useful function")
    print("2. Print trail name")
    print("3. Print hikername")
    print("4. Print hikename")
    print("5. Add new trail")
    print("6. Find by trail id")
    print("7. Find by trail name")

if __name__ == "__main__":
    main()
