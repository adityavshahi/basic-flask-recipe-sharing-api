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
    return jsonify({'message': 'recipe not found .'}),HTTPStatus.NOT_FOUND

@app.route("/recipes",methods=["POST"])
def create_recipe():
    data = request.get_json()
    name = data.get("name")
    description = data.get("description")
    recipe = {
        'id': len(recipes) + 1,
        'name': name,
        'description': description
    }
    recipes.append(recipe)
    return jsonify(recipe),HTTPStatus.CREATED

@app.route("/recipes/<int:recipe_id>",methods=["PUT"])
def update_recipe(recipe_id):
    for recipe in recipes:
        if recipe['id'] == recipe_id:
            data = request.get_json()
            recipe.update(
                {
                    "name": data.get("name"),
                    "description": data.get("description")
                }
            )
            return jsonify(recipe)
    return jsonify({"message": "recipe not found ."}),HTTPStatus.NOT_FOUND

@app.route("/recipes/<int:recipe_id>",methods=["DELETE"])
def delete_recipe(recipe_id):
    for recipe in recipes:
        if recipe['id'] == recipe_id:
            recipes.remove(recipe)
            return jsonify({"message": "Recipe Deletion Successful"})
    return jsonify({"message": "recipe not found ."}),HTTPStatus.NOT_FOUND