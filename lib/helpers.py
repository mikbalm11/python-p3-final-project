# lib/helpers.py

import random

from models.hiker import Hiker
from models.hike import Hike

def list_hiker_hikes():
    hikername = input("Please enter hiker name to list hikes completed: ")
    hiker = next((hiker for hiker in Hiker.get_all() if hiker.name == hikername), None)
    if hiker:
        print(f"Hiker {hiker.name} has completed the following hikes:")
        for hike in hiker.hikes():
            print(f"- {hike.trail_name}")
    else:
        print("Hiker not found.")

def hikername():
    for hiker in Hiker.get_all():
        print(hiker)

def hikename():
    for hike in Hike.get_all():
        print(hike)

def add_hike():
    # renamed to "add_hike" functionality
    hikername = input("Enter hiker name: ")
    trail_name = input("Enter trail name: ")
    hiker = next((h for h in Hiker.get_all() if h.name == hikername), None)
    if hiker:
        hike = Hike.create(trail_name, hiker)
        print(f"Hike created: {hike}")
    else:
        print("Hiker not found.")

# def find_trail_by_id():
#     searched_trail_id = int(input("Please enter id of the trail searched: "))
#     print(Trail.find_by_id(searched_trail_id))

# def find_trail_by_name():
#     searched_trail_name = input("Please enter name of the trail searched: ")
#     output = Trail.find_by_name(searched_trail_name)
#     if output:
#         print(output)
#     else:
#         print("Could not find trail with entered name.")
    
# def update_trail_name():
#     searched_trail_id = int(input("Please enter id of the trail searched: "))
#     output = Trail.find_by_id(searched_trail_id)
#     if output:
#         new_name = input("Enter the trails's new name: ")
#         output.name = new_name
#         output.update()
#         print(f"Success: {output}")
#     else:
#         print("Error updating trail name")

def exit_program():
    print("Goodbye!")
    exit()
