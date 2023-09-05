from flask import Flask,jsonify,request
from http import HTTPStatus


app = Flask(__name__)

recipes = [
    {
        'id': 1,
        'name': 'Egg Salad',
        'description': 'This is a lovely egg salad recipe.'
    },
    {
        'id': 2, 
        'name': 'Tomato Pasta',
        'description': 'This is a lovely tomato pasta recipe.'
    }
]

@app.route("/recipes",methods=["GET"])
def get_recipes():
    return jsonify({"recipes" : recipes})

@app.route("/recipes/<int:recipe_id>",methods=["GET"])
def get_recipe(recipe_id):
    for recipe in recipes:
        if recipe['id'] == int(recipe_id):
            return jsonify(recipe)
    return jsonify({'message': 'recipe not found .'})