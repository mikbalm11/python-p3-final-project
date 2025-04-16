# lib/helpers.py

from models.hiker import Hiker
from models.hike import Hike

def list_hikes(hiker_id):
    hiker = next((hiker for hiker in Hiker.all_hikers() if hiker.id == hiker_id), None)
    if hiker:
        if hiker.hikes():
            print(f"Hiker {hiker.name} has completed the following hikes:")
            for hike in hiker.hikes():
                print(f"{hike.id}. {hike.trail_name}")
        else:
            print("This hiker has not yet completed any hikes.")
    else:
        print("Hiker not found.")

def hikername():
    for hiker in Hiker.all_hikers():
        print(f"\t\t{hiker}")

# def hikename():
#     for hike in Hike.get_all():
#         print(f"\t\t{hike}")

def add_hike(hiker_id):
    # renamed to "add_hike"
    trail_name = input("Enter trail name completed by this hiker: ")
    hiker = next((h for h in Hiker.all_hikers() if h.id == hiker_id), None)
    if hiker:
        hike = Hike.create(trail_name, hiker)
        print(f"Hike created: {hike}")
    else:
        print("There was a problem finding hiker. Trail could not be added.")

def update_hike(hike_id):
    try:
        hike = Hike.find_by_id(hike_id)
        if not hike:
            print("No hike found with that ID.")
            return

        print(f"Current hike: {hike}")

        new_trail_name = input("Enter new trail name (leave blank to keep current): ")
        new_trail_name = new_trail_name if new_trail_name else hike.trail_name

        hike.trail_name = new_trail_name
        hike.update()

    except ValueError:
        print("Please enter a valid hike ID.")

def delete_hike(hike_id):
    try:
        hike = Hike.find_by_id(hike_id)
        if hike:
            hike.delete()
        else:
            print("No hike found with that ID.")
    except ValueError:
        print("Please enter a valid integer ID.")

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
    output = Hiker.find_by_id(searched_hike_id)
    if output:
        return output
    else:
        print("Could not find hiker with entered id. You can list all hiker information using 'Print hiker names' option.")

def update_hiker_name(searched_hiker_id):
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
