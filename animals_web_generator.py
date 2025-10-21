import json

def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)

def print_animal_data(animals_data):
    """Iterates through animals and prints selected info"""
    for animal in animals_data:

        name = animal["name"]
        diet = animal["characteristics"]["diet"]
        locations = animal["locations"]
        animal_type = animal.get("characteristics").get("type")

        if name:
            print(f"Name: {name}")
        if diet:
            print(f"Diet: {diet}")
        if locations and len(locations) > 0:
            print(f"Location: {locations[0]}")
        if animal_type:
            print(f"Type: {animal_type}")

        print()

if __name__ == "__main__":
    animals_data = load_data("../test-zootopia/animals_data.json")
    print_animal_data(animals_data)