import json
import os
from pathlib import Path


class Ingredients:
    def __init__(self):
        PATH = 'data/db/ofw.json'

        try:
            with open(PATH, 'r') as file:
                self.data = json.load(file)
                print(f'Load Successful: {PATH}')
        except FileNotFoundError:
            print(f'File not Found: {PATH}')
        except Exception as e:
            print(f'An unexpected error occurred: {e}')

        self.ing = None
        self.percentage = 1.0
        self.name = None
        self.ofw_values = None
        self.ofw_val_int = None

    def set_percentage(self, n):
        self.percentage = n

    def check_available(self, item):
        try:
            for ing in self.data:
                if ing['name'] == item:
                    return True
        except Exception as e:
            print(f"Ingredient not found: {e}")
        return False

    def get_ingredient(self, name, percentage=1.0):
        try:
            for ing, n in enumerate(self.data):
                if self.data[ing]["name"] == name:
                    weighted_ingredient = self.data[ing]
                    for item, value in weighted_ingredient.items():
                        if item == "name":
                            continue
                        else:
                            weighted_ingredient[item] = float(weighted_ingredient[item]) * percentage
                    return weighted_ingredient
        except FileNotFoundError:
            print('ERROR: File not Found')
        except AttributeError as e:
            print(f'ERROR: {e} not found')

    def list_ingredients(self) -> list:
        ingredient_names = []
        for i, val in enumerate(self.data):
            ingredient_names.append(self.data[i]['name'])
        return ingredient_names
