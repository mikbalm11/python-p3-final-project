# lib/cli.py

from helpers import (
    exit_program,
    hikername,
    hikename,
    list_hikes,
    add_hike,
    add_hiker,
    find_hiker_by_id,
    find_hiker_by_name,
    update_hiker_name,
    update_hiker_age
)

def main():
    while True:
        main_menu()
        choice = input("> ").lower()
        if choice == "e":
            exit_program()
        elif choice == "1":
            list_hikes()
        elif choice == "h":
            hikername()
            hiker_menu_1 = True
            while hiker_menu_1:
                hikermenu_1()
                choice = input("> ").lower()
                # print(f'my input is {choice} with typeof {type(choice)}')
                if choice == "b":
                    hiker_menu_1 = False
                elif choice == "a":
                    add_hiker()
                    hikername()
                elif choice.isdigit():
                    hiker_id = int(choice)
                    shown_hiker = find_hiker_by_id(hiker_id)
                    if shown_hiker:
                        print(shown_hiker)
                        list_hikes(shown_hiker.id)
                        hiker_menu_2 = True
                        while hiker_menu_2:
                            hikermenu_2()
                            choice_hm2 = input("> ").lower()
                            if choice_hm2 == "b":
                                hiker_menu_2 = False
                            elif choice_hm2 == "n":
                                update_hiker_name(hiker_id)
                            elif choice_hm2 == "a":
                                update_hiker_age(hiker_id)
                            else:
                                invalid()
                else:
                    invalid()
        elif choice == "3":
            hikename()
        elif choice == "4":
            add_hike()
        elif choice == "7":
            find_hiker_by_name()
        else:
            invalid()

def main_menu():
    print("\n")
    print("\tPlease select an option:")
    print("\t\t* type h to see the hikers")
    print("\t\t* type e to exit")
    print("\n")
    # print("1. List hiker's completed trails")
    # print("2. Print hiker names")
    # print("3. Print hike records")
    # print("4. Add new hike")
    # print("6. Find hiker by id")
    # print("7. Find hiker by name")

def hikermenu_1():
    print("\n")
    # print("\t\thikermenu_1")
    print("\t\t\t* type hiker id to see hikes")
    print("\t\t\t* type a to add new hiker")
    print("\t\t\t* type b to go back")
    print("\n")

def hikermenu_2():
    print("\n")
    # print("\t\t\thikermenu_2")
    print("\t\t\t\t* type n to update hiker name")
    print("\t\t\t\t* type a to update hiker age")
    print("\t\t\t\t* type b to go back")
    print("\n")

def go_back():
    return 

def invalid():
    print("\n")
    print("Invalid choice")

if __name__ == "__main__":
    main()
