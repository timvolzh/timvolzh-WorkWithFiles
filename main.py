from pprint import pprint

def get_recipes(path_to_recipes):
    recipes = {}
    with open(path_to_recipes, 'r', encoding="utf-8") as file:
        for line in file:
            dish = line.strip()
            amount_of_ingredients = int(file.readline())
            ingredients_list = []
            for item in range(amount_of_ingredients):
              name, quantity, measure = file.readline().split('|')
              ingredients_list.append({'ingredient_name': name.strip(), 'quantity': quantity.strip(), 'measure': measure.strip()})
            recipes[dish] = ingredients_list

            file.readline()
    return recipes


def get_shop_list_by_dishes(dishes, person_count):
    recipes = get_recipes("Cook_book.txt")
    shop_dict = {}
    for dish in dishes:
      dish_dict = recipes[dish]
      for ingredient in dish_dict:
        if ingredient['ingredient_name'] in shop_dict:
          (shop_dict[ingredient['ingredient_name']])['quantity'] += int(ingredient['quantity']) * person_count 
        else: shop_dict[ingredient['ingredient_name']] = {'measure': ingredient['measure'], 'quantity' : int(ingredient['quantity']) * person_count}
    return shop_dict


# Проверка кода
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 3))
