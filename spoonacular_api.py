
# https://api.spoonacular.com/recipes/findByIngredients?ingredients=apples,+flour,+sugar&number=5&apiKey=6bc2ab01d9814ba595912f83fba74cd1

# from  urllib import parse, request
# import json
# import spoontacular_api as sp
import requests

KEY = "apiKey=b9ab8744ef5c4d319495d24f2f2d8544"
BASE_URL = "https://api.spoonacular.com/recipes/findByIngredients?"
PARAMETERS = "ingredients=apples&number=1"


def user_ingredients(ingredients):
    pass




def build_url():
    headers = {'Content-Type': 'application/json'}
    print(BASE_URL + PARAMETERS+"&" + KEY)
    request = requests.get(BASE_URL + PARAMETERS +"&" + KEY, headers=headers)
    response_json = request.json()
    request.close()
    

if __name__ == "__main__":
    #ingredients = get_input()
    ingredients = "apple, flour, sugar"
    user_ingredients(ingredients)
    build_url()
