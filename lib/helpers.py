# lib/helpers.py

from models.model_1 import Trail

def helper_1():
    print("Performing useful function#1.")

def trailname():
    t = Trail("Test trail")
    print(t)


def exit_program():
    print("Goodbye!")
    exit()
