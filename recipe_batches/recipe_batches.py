#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    # declare needed variable one to hold the accumulated value (batches) and one to hold
    # true (ready) while ingredients are available.
    batches, ready = 0, True
# use a while loop with a condition that ready is true
    while ready:
      # use keys of library to check if ingredients are still available
        for key in recipe:
            if key in ingredients:
                # check if we have required ingredients for the recipe
                if recipe[key] <= ingredients[key]:
                  # deduct the required ingredients from the ingredients dictionairy
                    ingredients[key] = ingredients[key] - recipe[key]
                # if ingredients were not greater than recipe toggle ready to false.
                else:
                    ready = False
            # if the ingredient was not available in dictionairy then toggle ready to false.
            else:
                ready = False
        if ready:
            batches += 1
    return batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
