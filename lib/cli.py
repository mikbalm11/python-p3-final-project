# lib/cli.py

from helpers import (
    exit_program,
    hikername,
    hikename,
    list_hiker_hikes,
    add_hike
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
            hikername()
        elif choice == "3":
            hikename()
        elif choice == "4":
            add_hike()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List hiker's completed trails")
    print("2. Print hiker names")
    print("3. Print hike records")
    print("4. Add new hike")

if __name__ == "__main__":
    main()
