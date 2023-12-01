from src.classes.ingredients import Ingredients


class Recipe(Ingredients):
    def __init__(self):
        super().__init__()

    def sum_recipe(self, recipe_list: list) -> dict:
        sum_list = {'lauric': 0,
                    'myristic': 0,
                    'palmitic': 0,
                    'stearic': 0,
                    'ricinoleic': 0,
                    'oleic': 0,
                    'linoleic': 0,
                    'linolenic': 0}

        for key in recipe_list:
            if key is not None:
                cur_item = list(key.values())[1:]
                sum_list['lauric'] += cur_item[0]
                sum_list['myristic'] += cur_item[1]
                sum_list['palmitic'] += cur_item[2]
                sum_list['stearic'] += cur_item[3]
                sum_list['ricinoleic'] += cur_item[4]
                sum_list['oleic'] += cur_item[5]
                sum_list['linoleic'] += cur_item[6]
                sum_list['linolenic'] += cur_item[7]

        return sum_list
