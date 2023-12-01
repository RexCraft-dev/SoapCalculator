from src.classes.recipe import Recipe


recipe_list = []
recipe = Recipe()
ingredients = recipe.list_ingredients()

recipe_remainder = 0.2

recipe_list.append(recipe.get_ingredient("Canola Oil", percentage=0.4))
recipe_list.append(recipe.get_ingredient("Almond Butter", percentage=0.4))

list_sum = recipe.sum_recipe(recipe_list)

for ingredient in ingredients:
    recommendations = []

    curr_ingredient = recipe.get_ingredient(ingredient, recipe_remainder)
    if list_sum['oleic'] + curr_ingredient['oleic'] <= 48.0:
        recommendations.append(ingredient)
        print(curr_ingredient['name'])






