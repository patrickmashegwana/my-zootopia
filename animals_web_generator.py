"""
This module provides functionality to load data from a file, format specific
data into HTML, and generate an HTML file based on template replacement.
"""
import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)


def read_html_file():
    """Read the content of the html template"""
    with open("animals_template.html", "r") as file:
        return file.read()


def write_html_file(new_html):
    """Write the content of the html template"""
    with open("animals.html", "w") as file:
        file.write(new_html)


def serialize_animal(animal_obj):
    """Serializes an animal object into a string."""

    output = ''
    output += '<li class="cards__item">'
    output += (f'<div class="card__title">{animal_obj["name"]} '
               f'({animal_obj["taxonomy"]["scientific_name"]})</div>\n')
    if 'slogan' in animal_obj['characteristics']:
        output += f'<p class="card__text"><em>{animal_obj["characteristics"]["slogan"]}</em></p>'
    output += '<div class="card__text">'
    output += '<ul>'
    output += f"<li><strong>Diet:</strong> {animal_obj['characteristics']['diet']}</li>\n"
    output += f"<li><strong>Location:</strong> {animal_obj['locations'][0]}</li>\n"
    if 'type' in animal_obj['characteristics']:
        output += f"<li><strong>Type:</strong> {animal_obj['characteristics']['type']}</li>\n"
    output += '</ul>'
    output += "</div>"
    output += "</li>"

    return output


def create_animals_html(animals_data):
    """Fetches and formats animal data into HTML list item strings."""
    output = ""
    for animal in animals_data:
        output += serialize_animal(animal)

    return output


def main():
    """Main function."""
    animals_data = load_data("animals_data.json")
    result = read_html_file()
    data = create_animals_html(animals_data)

    result = result.replace("__REPLACE_ANIMALS_INFO__", data)

    write_html_file(result)


if __name__ == "__main__":
    main()
