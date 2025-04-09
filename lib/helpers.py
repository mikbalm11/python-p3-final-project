# lib/helpers.py

import random

from models.model_1 import Trail
from models.model_1 import Hiker
from models.model_1 import Hike

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

def exit_program():
    print("Goodbye!")
    exit()
