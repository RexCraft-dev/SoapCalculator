import json
from src.classes.ingredients import Ingredients
from src.classes.recipe import Recipe


ingredients = Ingredients()
recipe = Recipe()

ingredient_list = []

recipe.add_ingredient(ingredients.get_ingredient("Canola Oil", percentage=0.5))
recipe.add_ingredient(ingredients.get_ingredient("Baobab Oil", percentage=0.5))

total = recipe.sum_recipe()

print(total)


