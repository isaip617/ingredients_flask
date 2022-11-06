from flask import render_template, redirect, url_for, request
from app import app

import requests

KEY = "apiKey=af92a69ca7cb4348a5ab3afb2ff3dc71"
BASE_URL = "https://api.spoonacular.com/recipes/"

def build_url(query):
    headers = {'Content-Type': 'application/json'}
    request = requests.get(BASE_URL + query + KEY, headers=headers)
    response_json = request.json()
    request.close()
    return response_json


def format_input(ing_input): 

# ImmutableMultiDict([('ingredients', 'apples, flour, sugar'), ('meal3', 'Snack'), ('meal4', 'Dessert')])

    ing_str = ing_input["ingredients"]
    ing_str = ing_str.replace(' ', '+')
    first_recipe_search = build_url("" + ing_str, "findByIngredients?sort=min-missing-ingredients&ingredients=" + ing_str + "&number=10&")


    filter_dict = {}
    for recipe in first_recipe_search:
        inner_dict = {}
        for parameter in recipe.keys():
            if parameter == "id": 
                newkey = parameter
            elif parameter == "title":
                inner_dict[parameter] = recipe[parameter]
            elif parameter in ["missedIngredients", "usedIngredients"]:
                ingredient_names_dict = {}
                for p in parameter:
                    if p in ["original", "name"]:
                        ingredient_names_dict[p] = parameter[p]

        filter_dict[newkey] = inner_dict
    
    meal_type = ing_input["meal_type"]
    

    diet_res = ing_input["diet"]

    new_filtered_dict = {}
    for id_num, recipe_value in filter_dict.items():
        search_recipe = build_url(id_num + "/information?")
        # check if diet and meal type are what the user wants
        d = 0
        
        for key, value in search_recipe.items():
            if key == diet_res:
                if key:
                    diet_valid = True
                else: diet_valid = False
            elif key == "dishTypes":
                if meal_type in value:
                    meal_valid = True
                else:
                    meal_valid = False
        
        if meal_valid and diet_valid:
            # add to second new filtered dictionary
            new_filtered_dict[key] = value
            # add instructions to new dictionary
            new_filtered_dict[id_num]["instructions"] = search_recipe["instructions"]
            new_filtered_dict[id_num]["image"] = search_recipe["image"]



@app.route('/index', methods =['POST', 'GET'])
def index():
    if request.method == 'POST':

        print(request.form)

        # request form looks like this ImmutableMultiDict([('ingredients', 'apples, flour, sugar'), ('meal3', 'Snack'), ('meal4', 'Dessert')])

        #format_input(request.form) # ingredients input


        

    return render_template('index.html', title='Home')
