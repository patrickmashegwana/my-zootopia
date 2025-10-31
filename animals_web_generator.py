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
        output += '<li class="cards__item">'
        output += f"Name: {animal['name']}<br/>\n"
        output += f"Diet: {animal['characteristics']['diet']}<br/>\n"
        output += f"Location: {animal['locations'][0]}<br/>\n"
        if 'type' in animal['characteristics']:
            output += f"Type: {animal['characteristics']['type']}<br/>\n"
        output += '</li>'

    return output

if __name__ == "__main__":
    animals_data = load_data("animals_data.json")
    result = read_html_file()
    data = print_animal_data(animals_data)

    result = result.replace("__REPLACE_ANIMALS_INFO__", data)

    write_html_file(result)

