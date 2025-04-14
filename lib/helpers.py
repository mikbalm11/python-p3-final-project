# lib/helpers.py

import random

from models.trail import Trail
from models.hiker import Hiker
from models.hike import Hike

def list_hiker_hikes():
    hikername = input("Please enter hiker name to list hikes completed: ")
    hiker = next((hiker for hiker in Hiker.get_all() if hiker.name == hikername), None)
    if hiker:
        print(f"Hiker {hiker.name} has completed the following hikes:")
        for hike in hiker.hikes():
            print(hike)

def trailname():
    trails = Trail.get_all()
    for trail in trails:
        print(trail)

def hikername():
    hikers = Hiker.get_all()
    for hiker in hikers:
        print(hiker)

def hikename():
    hikes = Hike.get_all()
    for hike in hikes:
        print(hike)

def add_trail():
    new_trail_name = input("Please enter new trail name: ")
    new_trail = Trail.create(new_trail_name)
    print(new_trail)

def find_trail_by_id():
    searched_trail_id = int(input("Please enter id of the trail searched: "))
    print(Trail.find_by_id(searched_trail_id))

def find_trail_by_name():
    searched_trail_name = input("Please enter name of the trail searched: ")
    output = Trail.find_by_name(searched_trail_name)
    if output:
        print(output)
    else:
        print("Could not find trail with entered name.")
    
def update_trail_name():
    searched_trail_id = int(input("Please enter id of the trail searched: "))
    output = Trail.find_by_id(searched_trail_id)
    if output:
        new_name = input("Enter the trails's new name: ")
        output.name = new_name
        output.update()
        print(f"Success: {output}")
    else:
        print("Error updating trail name")

def exit_program():
    print("Goodbye!")
    exit()
