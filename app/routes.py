from flask import render_template, redirect, url_for, request
from app import app

#@app.route('/')
@app.route('/index', methods =['POST', 'GET'])
def index():
    if request.method == 'POST':
        print(request.form)

        #return redirect(url_for('found_recipes', recipes = recipes))

    
    return render_template('index.html', title='Home')

@app.route('/found_recipes')
def found_recipes():
    ingredients = "apple, flour, sugar"
    recipes = [{'id': 633547, 'title': 'Baked Cinnamon Apple Slices', 
    'image': 'https://spoonacular.com/recipeImages/633547-312x231.jpg', 'imageType': 'jpg', 
    'usedIngredientCount': 1, 'missedIngredientCount': 2, 'missedIngredients': [{'id': 2010, 
    'amount': 1.5, 'unit': 'tablespoons', 'unitLong': 'tablespoons', 'unitShort': 'Tbsp', 
    'aisle': 'Spices and Seasonings', 'name': 'cinnamon', 'original': '1 1/2 tablespoons of Cinnamon', 
    'originalName': 'Cinnamon', 'meta': [], 
    'image': 'https://spoonacular.com/cdn/ingredients_100x100/cinnamon.jpg'}, 
    {'id': 9299, 'amount': 0.5, 'unit': 'cup', 'unitLong': 'cups', 
    'unitShort': 'cup', 'aisle': 'Dried Fruits;Produce;Baking', 'name': 'raisins', 
    'original': '1/2 cup of Raisins', 'originalName': 'Raisins', 'meta': [], 
    'image': 'https://spoonacular.com/cdn/ingredients_100x100/raisins.jpg'}], 
    'usedIngredients': [{'id': 9003, 'amount': 4.0, 'unit': '', 'unitLong': '', 
    'unitShort': '', 'aisle': 'Produce', 'name': 'apples', 'original': 
    '4 Apples Sliced and Peeled – whatever type of apples I have in my refrigerator', 
    'originalName': 'Apples Sliced and Peeled – whatever type of apples I have in my refrigerator', 
    'meta': ['peeled', 'sliced'], 'image': 'https://spoonacular.com/cdn/ingredients_100x100/apple.jpg'}], 
    'unusedIngredients': [], 'likes': 1}]

    return render_template('found_recipes.html', title = "Found Recipes", recipes = recipes, ingredients = ingredients)

@app.route('/found_recipes/<int:Recipe_ID>')
def show_recipe(Recipe_ID):
    # search ingredient list 
    recipe = {'id': 633547, 'title': 'Baked Cinnamon Apple Slices', 
    'image': 'https://spoonacular.com/recipeImages/633547-312x231.jpg', 'imageType': 'jpg', 
    'usedIngredientCount': 1, 'missedIngredientCount': 2, 'missedIngredients': [{'id': 2010, 
    'amount': 1.5, 'unit': 'tablespoons', 'unitLong': 'tablespoons', 'unitShort': 'Tbsp', 
    'aisle': 'Spices and Seasonings', 'name': 'cinnamon', 'original': '1 1/2 tablespoons of Cinnamon', 
    'originalName': 'Cinnamon', 'meta': [], 
    'image': 'https://spoonacular.com/cdn/ingredients_100x100/cinnamon.jpg'}, 
    {'id': 9299, 'amount': 0.5, 'unit': 'cup', 'unitLong': 'cups', 
    'unitShort': 'cup', 'aisle': 'Dried Fruits;Produce;Baking', 'name': 'raisins', 
    'original': '1/2 cup of Raisins', 'originalName': 'Raisins', 'meta': [], 
    'image': 'https://spoonacular.com/cdn/ingredients_100x100/raisins.jpg'}], 
    'usedIngredients': [{'id': 9003, 'amount': 4.0, 'unit': '', 'unitLong': '', 
    'unitShort': '', 'aisle': 'Produce', 'name': 'apples', 'original': 
    '4 Apples Sliced and Peeled – whatever type of apples I have in my refrigerator', 
    'originalName': 'Apples Sliced and Peeled – whatever type of apples I have in my refrigerator', 
    'meta': ['peeled', 'sliced'], 'image': 'https://spoonacular.com/cdn/ingredients_100x100/apple.jpg'}], 
    'unusedIngredients': [], 'likes': 1}

    return render_template('individual_recipes.html', title=Recipe_ID, recipe = recipe) 