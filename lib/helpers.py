# lib/helpers.py

import random

from models.hiker import Hiker
from models.hike import Hike

def list_hikes(hiker_id):
    hiker = next((hiker for hiker in Hiker.all_hikers() if hiker.id == hiker_id), None)
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
    # renamed to "add_hike"
    hikername = input("Enter hiker name: ")
    trail_name = input("Enter trail name: ")
    hiker = next((h for h in Hiker.get_all() if h.name == hikername), None)
    if hiker:
        hike = Hike.create(trail_name, hiker)
        print(f"Hike created: {hike}")
    else:
        # have user create the hiker first
        print("Hiker not found. Please add the hiker first using the 'Add hiker' option.")

def add_hiker():
    name = input("Enter hiker's name: ")
    age_input = input("Enter hiker's age: ")

    try:
        age = int(age_input)
        new_hiker = Hiker.create(name, age)
        print(f"Hiker added: {new_hiker}")
    except ValueError:
        print("Age must be a number.")
    except Exception as e:
        print(f"Error adding hiker: {e}")

def find_hiker_by_id(searched_hike_id):
    # searched_hike_id = int(input("Please enter id of the hiker searched: "))
    output = Hiker.find_by_id(searched_hike_id)
    if output:
        return output
    else:
        print("Could not find hiker with entered id. You can list all hiker information using 'Print hiker names' option.")

def find_hiker_by_name():
    searched_hike_name = input("Please enter name of the hiker searched: ")
    output = Hiker.find_by_name(searched_hike_name)
    if output:
        print(output)
    else:
        print("Could not find hiker with entered name. You can list all hiker information using 'Print hiker names' option.")
    
def update_hiker_name(searched_hiker_id):
    # searched_hiker_id = int(input("Please enter id of the hiker searched: "))
    output = Hiker.find_by_id(searched_hiker_id)
    if output:
        new_name = input("Enter the hiker's new name: ")
        output.name = new_name
        output.update()
        print(f"Success: {output}")
    else:
        print("Error updating hiker name")

def update_hiker_age(searched_hiker_id):
    output = Hiker.find_by_id(searched_hiker_id)
    if output:
        new_age = int(input("Enter the hiker's new age: "))
        output.age = new_age
        output.update()
        print(f"Success: {output}")
    else:
        print("Error updating hiker name")

def exit_program():
    print("Goodbye!")
    exit()
