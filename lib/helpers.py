# lib/helpers.py

import random

from models.model_1 import Trail
from models.model_1 import Hiker
from models.model_1 import Hike

# # Create 20 Trail instances
# trail_names = ["Sunset Ridge", "Rocky Path", "Pine Valley", "Bear Creek", "Eagle Summit", "Hidden Falls", "Wildflower Trail", "Misty Woods", "Canyon Loop", "Maple Pass", "Silver Lake", "Golden Peak", "Shadow Mountain", "Crystal Springs", "Lone Pine", "Blue Ridge", "Thunder Pass", "Highland Trek", "Serenity Trail", "Redwood Route"]
# trails = [Trail(name) for name in trail_names]

# # Create 20 Hiker instances
# hiker_names = ["John", "Emily", "Mike", "Sarah", "David", "Laura", "Chris", "Anna", "James", "Sophia", "Daniel", "Olivia", "Matthew", "Emma", "Andrew", "Isabella", "Ryan", "Mia", "Ethan", "Charlotte"]
# hikers = [Hiker(name, random.randint(18, 60)) for name in hiker_names]

# # Create 20 Hike instances, randomly assigning trails and hikers
# hikes = [Hike(random.choice(trails), random.choice(hikers)) for _ in range(20)]

# # t = Trail("Test trail")
# # h = Hiker("John Doe", 30)
# # k = Hike(t, h)

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

def exit_program():
    print("Goodbye!")
    exit()
