# lib/helpers.py

from models.model_1 import Trail
from models.model_1 import Hiker
from models.model_1 import Hike

t = Trail("Test trail")
h = Hiker("John Doe", 30)

def helper_1():
    print("Performing useful function#1.")

def trailname():
    print(t)

def hikername():
    print(h)

def hikename():
    hike = Hike(t, h)
    print(hike)

def exit_program():
    print("Goodbye!")
    exit()
