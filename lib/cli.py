# lib/cli.py

from helpers import (
    exit_program,
    trailname,
    hikername,
    hikename,
    helper_1
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            helper_1()
        elif choice == "2":
            trailname()
        elif choice == "3":
            hikername()
        elif choice == "4":
            hikename()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")
    print("2. Print trail name")
    print("3. Print hikername")
    print("4. Print hikename")


if __name__ == "__main__":
    main()
