import random


def generate_password(length=10, symbols=False, numbers=False, letters=False):
    characters = {
        'lowercase': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                      't', 'u', 'v', 'w', 'x', 'y', 'z'],
        'uppercase': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                      'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
        'numbers': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
        'symbols': ['!', '@', '#', '$', '%', '&', '?']
    }
    if not symbols and not numbers and not letters:
        return "Password needs characters"
    password = ""
    selected_characters = []
    if letters:
        selected_characters.extend(characters['lowercase'])
        selected_characters.extend(characters['uppercase'])
    if numbers:
        selected_characters.extend(characters["numbers"])
    if symbols:
        selected_characters.extend(characters["symbols"])

    for i in range(length):
        password += random.choice(selected_characters)
    return password


# generate_password(10, True, True, True)
