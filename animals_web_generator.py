import json

def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)


def read_html_file():
    '''Read the content of the htlm template'''
    with open("animals_template.html", "r") as file:
        return file.read()

def write_html_file(new_html):
    '''Write the content of the htlm template'''
    with open("animals.html", "w") as file:
        file.write(new_html)

def print_animal_data(animals_data):
    """Iterates through animals and prints selected info"""
    output = ""
    for animal in animals_data:

        name = animal["name"]
        diet = animal["characteristics"]["diet"]
        locations = animal["locations"]
        animal_type = animal.get("characteristics").get("type")

        if name:
            output += f"Name: {name}\n"
        if diet:
            output += f"Diet: {diet}\n"
        if locations and len(locations) > 0:
            output += f"Location: {locations[0]}\n"
        if animal_type:
            output += f"Type: {animal_type}\n"

    return output

if __name__ == "__main__":
    animals_data = load_data("../test-zootopia/animals_data.json")
    result = read_html_file()
    data = print_animal_data(animals_data)

    result = result.replace("__REPLACE_ANIMALS_INFO__", data)

    write_html_file(result)

