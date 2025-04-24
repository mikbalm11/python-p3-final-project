# lib/cli.py

from helpers import (
    list_all_hikers,
    add_hiker,
    find_hiker_by_id,
    list_hikes,
    update_hiker_name,
    update_hiker_age,
    add_hike,
    update_hike,
    delete_hike,
    delete_hiker,
    banner,
    main_menu,
    hikermenu_1,
    hikermenu_2,
    newline,
    invalid,
    exit_program
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
            list_all_hikers()
            hiker_menu_1 = True
            while hiker_menu_1:
                hikermenu_1()
                choice = input("> ").lower()
                if choice == "b":
                    hiker_menu_1 = False
                    newline()
                    list_all_hikers()
                elif choice == "a":
                    add_hiker()
                    newline()
                    list_all_hikers()
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
                                list_all_hikers()
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
                                list_all_hikers()
                            elif choice_hm2 == "e":
                                exit_program()
                            else:
                                invalid()
                elif choice == "e":
                    exit_program()
                else:
                    invalid()
        else:
            invalid()

if __name__ == "__main__":
    main()
