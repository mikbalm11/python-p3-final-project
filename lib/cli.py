# lib/cli.py

from helpers import (
    exit_program,
    hikername,
    list_hikes,
    add_hike,
    update_hike,
    delete_hike,
    add_hiker,
    find_hiker_by_id,
    update_hiker_name,
    update_hiker_age,
    delete_hiker,
)

def main():
    while True:
        newline()
        banner()
        main_menu()
        choice = input("> ").lower()
        if choice == "e":
            newline()
            exit_program()
        elif choice == "h":
            newline()
            hikername()
            hiker_menu_1 = True
            while hiker_menu_1:
                hikermenu_1()
                choice = input("> ").lower()
                # print(f'my input is {choice} with typeof {type(choice)}')
                if choice == "b":
                    hiker_menu_1 = False
                    newline()
                    hikername()
                elif choice == "a":
                    add_hiker()
                    newline()
                    hikername()
                elif choice.isdigit():
                    newline()
                    hiker_id = int(choice)
                    shown_hiker = find_hiker_by_id(hiker_id)
                    if shown_hiker:
                        print(shown_hiker)
                        newline()
                        list_hikes(shown_hiker.id)
                        hiker_menu_2 = True
                        while hiker_menu_2:
                            hikermenu_2()
                            choice_hm2 = input("> ").lower()
                            if choice_hm2 == "b":
                                hiker_menu_2 = False
                                hikername()
                            elif choice_hm2 == "n":
                                update_hiker_name(hiker_id)
                                newline()
                                list_hikes(hiker_id)
                            elif choice_hm2 == "a":
                                update_hiker_age(hiker_id)
                                newline()
                                list_hikes(hiker_id)
                            elif choice_hm2 == "h":
                                add_hike(hiker_id)
                                newline()
                                list_hikes(hiker_id)
                            elif choice_hm2 == "u":
                                choice_hike_id = int(input("Please enter hike number to update: "))
                                update_hike(choice_hike_id)
                                newline()
                                list_hikes(hiker_id)
                            elif choice_hm2 == "d":
                                choice_hike_id = int(input("Please enter hike number to delete: "))
                                delete_hike(choice_hike_id)
                                newline()
                                list_hikes(hiker_id)
                            elif choice_hm2 == "r":
                                delete_hiker(hiker_id)
                                hiker_menu_2 = False
                                newline()
                                hikername()
                            else:
                                invalid()
                else:
                    invalid()
        # elif choice == "a":
        #     hikename()
        else:
            invalid()

def banner():
    """Prints a simple banner."""
    print(r"""TRAILMANAGER CLI - HIKE SMART, HIKE PROUD 🌲""")

def main_menu():
    """Program is initiated, lists simple options to list all hikers or exit the program."""
    newline()
    print("Please select an option:")
    print("\t* type h to see all hikers")
    print("\t* type e to exit")
    newline()

def hikermenu_1():
    """List hikers option is selected, lists all hikers and an option to add one, also an option to go back."""
    newline()
    print("\t\t* type hiker number to see their hikes")
    print("\t\t* type a to add new hiker")
    print("\t\t* type b to go back")
    newline()

def hikermenu_2():
    """A hiker number - ID is selected and their hikes are listed, lists a bunch of CRUD options on both the hiker itself and their hikes."""
    newline()
    print("\t\t\t* type n to update hiker name")
    print("\t\t\t* type a to update hiker age")
    print("\t\t\t* type h to add a new hike completed by this hiker")
    print("\t\t\t* type u to update a hike completed by this hiker")
    print("\t\t\t* type d to delete a hike completed by this hiker")
    print("\t\t\t* type r to remove this hiker and their hikes")
    print("\t\t\t* type b to go back")
    newline()

def invalid():
    """And invalid selection is made, prompts the user as such. """
    newline()
    print("Invalid choice")
    
def newline():
    """Prints a new line."""
    print("\n")

if __name__ == "__main__":
    main()
