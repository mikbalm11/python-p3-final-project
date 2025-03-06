# lib/helpers.py

from models.model_1 import Trail
from models.model_1 import Hiker

def helper_1():
    print("Performing useful function#1.")

def trailname():
    t = Trail("Test trail")
    print(t)

def hikername():
    h = Hiker("John Doe", 30)
    print(h)

def exit_program():
    print("Goodbye!")
    exit()
