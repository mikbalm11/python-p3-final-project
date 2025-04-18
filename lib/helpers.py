# lib/helpers.py

from models.hiker import Hiker
from models.hike import Hike

def hikername():
    """Prints the name of all hikers."""
    for hiker in Hiker.all_hikers():
        print(f"\t\t{hiker}")

def list_hikes(hiker_id):
    """Lists all hikes completed by a specific hiker."""
    hiker = next((hiker for hiker in Hiker.all_hikers() if hiker.id == hiker_id), None)
    if hiker:
        if hiker.hikes():
            print(f"Hiker {hiker.name} has completed the following hikes:")
            for hike in hiker.hikes():
                print(f"{hike.id:2}. {hike.trail_name}")
            print(f"Total hikes: {len(hiker.hikes())}")
        else:
            print("This hiker has not yet completed any hikes.")
    else:
        print("Hiker not found.")

def add_hike(hiker_id):
    """Adds a new hike for a specific hiker."""
    trail_name = input("Enter trail name completed by this hiker: ")
    hiker = next((h for h in Hiker.all_hikers() if h.id == hiker_id), None)
    if hiker:
        hike = Hike.create(trail_name, hiker)
        print(f"Hike created: {hike}")
    else:
        print("There was a problem finding hiker. Trail could not be added.")

def update_hike(hike_id):
    """Updates the details of a specific hike, allowing changes to the trail name."""
    try:
        hike = Hike.find_by_id(hike_id)
        if not hike:
            print("No hike found with that ID.")
            return

        print(f"Current hike: {hike}")

        new_trail_name = input("Enter new trail name: ")

        hike.trail_name = new_trail_name
        hike.update()

    except ValueError:
        print("Please enter a valid hike ID.")
    except Exception as e:
        print(f"Error updating hike: {e}")

def delete_hike(hike_id):
    """Deletes a specific hike by its ID - hike number for the CLI user."""
    try:
        hike = Hike.find_by_id(hike_id)
        if hike:
            hike.delete()
        else:
            print("No hike found with number entered.")
    except ValueError:
        print("Please enter a valid integer.")
    except Exception as e:
        print(f"Error deleting hike: {e}")

def add_hiker():
    """Adds a new hiker with their name and age."""
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
    """Finds and returns a hiker by their ID - hiker number for the CLI user."""
    output = Hiker.find_by_id(searched_hike_id)
    if output:
        return output
    else:
        print("Could not find hiker with entered id. You can list all hiker information using 'Print hiker names' option.")

def update_hiker_name(searched_hiker_id):
    """Updates the name of a hiker identified by their ID - hiker number for the CLI user."""
    output = Hiker.find_by_id(searched_hiker_id)
    if output:
        new_name = input("Enter the hiker's new name: ")
        output.name = new_name
        output.update()
        print(f"Success: {output}")
    else:
        print("Error updating hiker name")

def update_hiker_age(searched_hiker_id):
    """Updates the age of a hiker identified by their ID - hiker number for the CLI user."""
    output = Hiker.find_by_id(searched_hiker_id)
    if output:
        new_age = int(input("Enter the hiker's new age: "))
        output.age = new_age
        output.update()
        print(f"Success: {output}")
    else:
        print("Error updating hiker name")

def delete_hiker(hiker_id):
    try:
        hiker = Hiker.find_by_id(hiker_id)
        if hiker:
            confirm = input(f"Are you sure you want to delete hiker '{hiker.name}'? This will also delete all associated hikes. (y/n): ").strip().lower()
            if confirm == "y":
                hiker.delete()
                print(f"Hiker '{hiker.name}' has been deleted.")
            else:
                print("Deletion cancelled.")
        else:
            print("No hiker found with number entered.")
    except ValueError:
        print("Please enter a valid integer.")

def exit_program():
    """Exits the program with a goodbye message."""
    print("Goodbye. Thanks for choosing TrailManager!")
    exit()
