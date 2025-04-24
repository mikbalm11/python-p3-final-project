# lib/helpers.py

from models.hiker import Hiker
from models.hike import Hike

def list_all_hikers():
    """Prints the name of all hikers."""
    for hiker in Hiker.all_hikers():
        print(f"\t\t{hiker}")

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
        print("Could not find hiker with entered id. You can list all hiker information using 'see all hikers' option.")

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
        while True:
            new_age_input = input("Enter the hiker's new age: ")
            try:
                new_age = int(new_age_input)
                output.age = new_age
                output.update()
                print(f"Success: {output}")
                break
            except ValueError:
                print("Invalid input. Age must be a number.")
    else:
        print("Error updating hiker name")

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

def banner():
    """Prints a simple banner."""
    print(r"""TRAILMANAGER CLI - HIKE SMART, HIKE PROUD 🌲""")

def main_menu():
    """Program is initiated, lists simple options to list all hikers or exit the program."""
    newline()
    print("Please select an option:")
    print("\t* type h to see all hikers")
    print("\t* type e to exit")
    newline()

def hikermenu_1():
    """List hikers option is selected, lists all hikers and an option to add one, also an option to go back."""
    newline()
    print("\t\t* type hiker number to see their hikes")
    print("\t\t* type a to add new hiker")
    print("\t\t* type b to go back")
    print("\t\t* type e to exit")
    newline()

def hikermenu_2():
    """A hiker number - ID is selected and their hikes are listed, lists a bunch of CRUD options on both the hiker itself and their hikes."""
    newline()
    print("\t\t\t* type n to update hiker name")
    print("\t\t\t* type a to update hiker age")
    print("\t\t\t* type h to add a new hike completed by this hiker")
    print("\t\t\t* type u to update a hike completed by this hiker")
    print("\t\t\t* type d to delete a hike completed by this hiker")
    print("\t\t\t* type r to remove this hiker and their hikes")
    print("\t\t\t* type b to go back")
    print("\t\t\t* type e to exit")
    newline()

def newline():
    """Prints a new line."""
    print("\n")

def invalid():
    """Prompts the user that an invalid selection is made."""
    newline()
    print("Invalid choice")

def exit_program():
    """Exits the program with a goodbye message."""
    print("Goodbye. Thanks for choosing TrailManager!")
    exit()
