
import requests

from src.models.character import Character


BASE_URL = 'https://www.breakingbadapi.com/'

def test_breaking_bad_api():
    FIRST_NAME = 'Walter'
    LAST_NAME = 'White'

    ENDPOINT = 'api/characters?name={first_name}+{last_name}'
    URL = BASE_URL + ENDPOINT.format(first_name=FIRST_NAME, last_name=LAST_NAME)

    response = requests.get(URL)
    characters = response.json()

    print(characters[0]['birthday'])


def test_get_all_characters_information():
    ENDPOINT = 'api/characters'
    URL = BASE_URL + ENDPOINT

    response = requests.get(URL)
    data = response.json()

    characters = []

    for character in data:
        characters.append(Character.from_dict(character))

    for character in characters:
        print(f'Character name: "{character.name}"')
        print(f'Portrayed: "{character.portrayed}"')
        print(f'------------------------------------------')