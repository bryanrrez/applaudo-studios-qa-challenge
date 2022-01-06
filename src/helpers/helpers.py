
import json


def type_text(text, driver):
    with open('src/resources/key_codes.json', encoding='utf-8') as key_codes_file:
        key_codes = json.load(key_codes_file)

        for character in text:
            for key_code in key_codes:
                if character == key_code['character']:
                    driver.press_keycode(key_code['key_code'])