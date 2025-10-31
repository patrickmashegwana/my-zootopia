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

def create_animals_html(animals_data):
    """Iterates through animals and prints selected info"""
    output = ""
    for animal in animals_data:
        output += '<li class="cards__item">'
        output += (f'<div class="card__title">{animal["name"]} '
                   f'({animal["taxonomy"]["scientific_name"]})</div>\n')
        if 'slogan' in animal['characteristics']:
            output += f'<p class="card__text"><em>{animal["characteristics"]["slogan"]}</em></p>'
        output += '<div class="card__text">'
        output += '<ul>'
        output += f"<li><strong>Diet:</strong> {animal['characteristics']['diet']}</li>\n"
        output += f"<li><strong>Location:</strong> {animal['locations'][0]}</li>\n"
        if 'type' in animal['characteristics']:
            output += f"<li><strong>Type:</strong> {animal['characteristics']['type']}</li>\n"
        output += '</ul>'
        output += "</div>"
        output += "</li>"

    return output

if __name__ == "__main__":
    animals_data = load_data("animals_data.json")
    result = read_html_file()
    data = create_animals_html(animals_data)

    result = result.replace("__REPLACE_ANIMALS_INFO__", data)

    write_html_file(result)

