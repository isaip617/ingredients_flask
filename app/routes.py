from flask import render_template, redirect, url_for, request
from app import app
import requests

KEY = "apiKey=b9ab8744ef5c4d319495d24f2f2d8544"
BASE_URL = "https://api.spoonacular.com/recipes/"



def build_url(query):
    headers = {'Content-Type': 'application/json'}
    request = requests.get(BASE_URL + query + KEY, headers=headers)
    response_json = request.json()
    request.close()
    return response_json


def format_input(ing_input): 

# ImmutableMultiDict([('ingredients', 'apples, flour, sugar'), ('meal3', 'Snack'), ('meal4', 'Dessert')])
    #print("entered format_input")
    ing_str = ing_input["ingredients"]
    ing_str = ing_str.replace(' ', '+')
    first_recipe_search = build_url("findByIngredients?sort=min-missing-ingredients&ingredients=" + ing_str + "&number=10&")
    #print(first_recipe_search)
    #print("Before filter_dict")
    filter_dict = {}
    for recipe in first_recipe_search:
        inner_dict = {}
        for parameter in recipe.keys():
            if parameter == "id": 
                newkey = recipe[parameter]
            elif parameter == "title":
                inner_dict[parameter] = recipe[parameter]
            elif parameter in ["missedIngredients", "usedIngredients"]:
                ingredient_names_dict = {}
                for p in recipe[parameter]:
                    #print(p)
                    #print()
                    for i in p:
                        print(f'I: {i}')
                        if i in ["original", "name"]:
                            ingredient_names_dict[i] = p[i]
                inner_dict[parameter] = ingredient_names_dict
                print(f'RECIPE PARAMETER {recipe[parameter]}')
                print()
                print(f'INGREDIENT NAMES: {ingredient_names_dict}')
        print()
        print(f'INNER DICT: {inner_dict}')


        filter_dict[newkey] = inner_dict
        #print(filter_dict)
    #print("After filter_dict")
    meal_type = ing_input["meal_type"]
    
    print("Diet_res")
    diet_res = ing_input["diet"]
    #print("test")
    new_filtered_dict = {}
    for id_num, recipe_value in filter_dict.items():
        search_recipe = build_url(str(id_num) + "/information?")
        # check if diet and meal type are what the user wants
        diet_valid = False
        if diet_res == "None": diet_valid = True
        meal_valid = False
        
        for key, value in search_recipe.items():
            if key == diet_res:
                print("diet here")
                if value:
                    diet_valid = True
                else: diet_valid = False
            elif key == "dishTypes":
                print("dish here")
                if meal_type == "None":
                    meal_valid = True
                elif meal_type in value:
                    meal_valid = True
                
                else:
                    meal_valid = False
            #new_filtered_dict[key] = value
        
        if meal_valid and diet_valid:
            print("both true")
            # add to second new filtered dictionary
            # add instructions to new dictionary
            new_filtered_dict[id_num] = {}
            new_filtered_dict[id_num]["instructions"] = search_recipe["instructions"]
            new_filtered_dict[id_num]["image"] = search_recipe["image"]
            new_filtered_dict[id_num]["title"] = search_recipe["title"]
            #print(search_recipe)
            #print(search_recipe["missedIngredients"])
            #print(filter_dict)
            new_filtered_dict[id_num]["missedIngredients"] = filter_dict[id_num]["missedIngredients"]
            new_filtered_dict[id_num]["usedIngredients"] = filter_dict[id_num]["usedIngredients"]
            


    #print("Returning new dict")
    #print(new_filtered_dict)
    return new_filtered_dict

#@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/found_recipes', methods =['POST', 'GET'])
def found_recipes():
    if request.method == 'POST':
        #print(request.form)
        recipes = format_input(request.form) # ingredients input
 
    return render_template('found_recipes.html', title = "Found Recipes", recipes = recipes, ingredients = request.form["ingredients"])

@app.route('/found_recipes/<int:Recipe_ID>')
def show_recipe(Recipe_ID):
    # search ingredient list 
    recipe = build_url(str(Recipe_ID) + "/information?")
    placehold = ["apples", "flour", "sugar", "salt", "water", "bread"] 

    return render_template('individual_recipes.html', title=Recipe_ID, recipe = recipe, ingredients = placehold) 