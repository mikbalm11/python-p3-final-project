# lib/cli.py

from helpers import (
    exit_program,
    hikername,
    # hikename,
    list_hikes,
    add_hike,
    update_hike,
    delete_hike,
    add_hiker,
    find_hiker_by_id,
    update_hiker_name,
    update_hiker_age
)

def main():
    while True:
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
                    hikername()
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
                                hikername()
                            elif choice_hm2 == "n":
                                update_hiker_name(hiker_id)
                                list_hikes(hiker_id)
                            elif choice_hm2 == "a":
                                update_hiker_age(hiker_id)
                                list_hikes(hiker_id)
                            elif choice_hm2 == "h":
                                add_hike(hiker_id)
                                list_hikes(hiker_id)
                            elif choice_hm2 == "u":
                                choice_hike_id = int(input("Please enter hike number to update: "))
                                update_hike(choice_hike_id)
                                list_hikes(hiker_id)
                            elif choice_hm2 == "d":
                                choice_hike_id = int(input("Please enter hike number to delete: "))
                                delete_hike(choice_hike_id)
                                list_hikes(hiker_id)
                            else:
                                invalid()
                else:
                    invalid()
        # elif choice == "a":
        #     hikename()
        else:
            invalid()

def banner():
    print(r"""
                TRAILMANAGER CLI - HIKE SMART, HIKE PROUD 🌲
    """)

def main_menu():
    print("\n")
    print("Please select an option:")
    print("\t* type h to see all hikers")
    # print("\t* type a to see all hikes")
    print("\t* type e to exit")
    print("\n")

def hikermenu_1():
    print("\n")
    print("\t\t* type hiker number to see hikes")
    print("\t\t* type a to add new hiker")
    print("\t\t* type b to go back")
    print("\n")

def hikermenu_2():
    print("\n")
    print("\t\t\t* type n to update hiker name")
    print("\t\t\t* type a to update hiker age")
    print("\t\t\t* type h to add a new hike completed by this hiker")
    print("\t\t\t* type u to update a hike completed by this hiker")
    print("\t\t\t* type d to delete a hike completed by this hiker")
    print("\t\t\t* type b to go back")
    print("\n")

def invalid():
    print("\n")
    print("Invalid choice")
    
def newline():
    print("\n")

if __name__ == "__main__":
    main()
