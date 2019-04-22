#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Import pre-requisites.                                                                                   #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

import os
from flask import Flask, render_template, redirect, request, url_for, request, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Connect to external MongoDB database through URI variable hosted on app server.                          #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'onlineCookbook'
app.config['MONGO_URI'] = os.environ.get('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Variables                                                                                                #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
recipes = mongo.db.recipes
recipeCategory = mongo.db.recipeCategory
allergens = mongo.db.allergens
skillLevel = mongo.db.skillLevel

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Homepage  - Load all recipes and load recipes to slider                                                  #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', recipes=recipes.find(), recipeCategory=recipeCategory.find())


@app.route('/get_recipes')
def get_recipes():
    return render_template('all_recipes.html', 
                            recipes = recipes.find(), recipeCategory=recipeCategory.find())

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Browse Recipes                                                                                           #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    
@app.route('/browse_recipes/<recipe_category_name>')
def browse_recipes(recipe_category_name):
    return render_template('browse_recipes.html',
    recipes=recipes.find({'recipe_category_name': recipe_category_name}), 
    recipeCategory=recipeCategory.find())
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Add Recipes                                                                                              #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#    

@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html', recipes=recipes.find(), recipeCategory=recipeCategory.find(), 
            skillLevel=skillLevel.find(), allergens=allergens.find())
            
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
        complete_recipe = {
            'recipe_name': request.form.get('recipe_name'),
            'recipe_description': request.form.get('recipe_description'),
            'recipe_category_name': request.form.get('recipe_category_name'),
            'allergen_type': request.form.getlist('allergen_type'),
            'recipe_prep_time': request.form.get('recipe_prep_time'),
            'recipe_cook_time': request.form.get('recipe_cook_time'),
            'recipe_serves': request.form.get('recipe_serves'),
            'recipe_difficulty': request.form.get('recipe_difficulty'),
            'recipe_image' : request.form.get('recipe_image'),            
            'recipe_ingredients':  request.form.getlist('recipe_ingredients'),
            'recipe_method':  request.form.getlist('recipe_method'),
            'featured_recipe':  request.form.get('featured_recipe'),
        }   
        recipes.insert_one(complete_recipe)
        return redirect(url_for('get_recipes'))
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Edit Recipes                                                                                             #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#    

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    return render_template('edit_recipe.html', recipeCategory=recipeCategory.find(), 
            allergens=allergens.find(), skillLevel=skillLevel.find(), recipes=recipes.find_one({'_id': ObjectId(recipe_id)}))
            
@app.route('/update_recipe', methods=['POST'])
def update_recipe():
        complete_recipe = {
            'recipe_name': request.form.get('recipe_name'),
            'recipe_description': request.form.get('recipe_description'),
            'recipe_category_name': request.form.get('recipe_category_name'),
            'allergen_type': request.form.getlist('allergen_type'),
            'recipe_prep_time': request.form.get('recipe_prep_time'),
            'recipe_cook_time': request.form.get('recipe_cook_time'),
            'recipe_serves': request.form.get('recipe_serves'),
            'recipe_difficulty': request.form.get('recipe_difficulty'),
            'recipe_ingredients':  request.form.getlist('recipe_ingredients'),
            'recipe_method':  request.form.getlist('recipe_method'),
            'featured_recipe': request.form.get('featured_recipe'),
            'recipe_image' : request.form.get('recipe_image')
        }
        recipes.insert_one(complete_recipe)
        return redirect(url_for('get_recipes'))        


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Individual Recipe Page                                                                                   #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    
@app.route('/recipe_page/<recipe_id>')
def recipe_page(recipe_id):
    return render_template('recipe.html', recipe=recipes.find_one({'_id': ObjectId(recipe_id)}), 
    recipeCategory=recipeCategory.find())

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Searching Keywords                                                                                       #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

@app.route('/search_keyword', methods=['POST'])
def receive_keyword():
    return redirect(url_for('search_keyword', keyword=request.form.get('keyword'))) 
    
    
@app.route('/search_keyword/<keyword>')
def search_keyword(keyword):
    recipes.create_index([('recipe_name', 'text'), 
        ('recipe_ingredients', 'text') ])
    return render_template('search_by_keyword.html', keyword=keyword, 
        search_results = recipes.find({'$text': {'$search': keyword}}), 
        recipeCategory=recipeCategory.find())

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Development/Production environment test for debug                                                        #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)