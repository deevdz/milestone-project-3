#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Import pre-requisites.                                                                                   #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

import os, pymongo, math
from flask import Flask, render_template, redirect, request, url_for, request, session, g, abort, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime, timedelta


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Connect to external MongoDB database through URI variable hosted on app server.                          #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'onlineCookbook'
app.config['MONGO_URI'] = os.environ.get('MONGO_URI', 'mongodb://localhost')

app.secret_key = os.getenv('SECRET', 'randomstring123')

mongo = PyMongo(app)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Variables                                                                                                #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
recipes = mongo.db.recipes
recipeCategory = mongo.db.recipeCategory
allergens = mongo.db.allergens
skillLevel = mongo.db.skillLevel
userDB = mongo.db.users

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Homepage  - Load all recipes and load recipes to slider                                                  #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
@app.route('/')
@app.route('/index/1')
def index():
    return render_template('index.html', recipes=recipes.find().sort('date_time',pymongo.DESCENDING), 
    recipeCategory=recipeCategory.find(), page=1)

@app.route('/get_recipes', methods=['GET','POST'])
def get_recipes():
    return render_template('all_recipes.html', recipes = recipes.find().sort('date_time',pymongo.DESCENDING), 
                            recipeCategory=recipeCategory.find(), page=1)
                            
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# User Login & Registration                                                                                #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# 
@app.route('/register')
def register():
    return render_template('register.html', recipes=recipes.find(), 
        recipeCategory=recipeCategory.find(), page=1)


@app.route('/signup', methods=['POST'])
def signup():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=30)
    author_name = request.form.get('author_name')
    username = request.form.get('username').lower()
    password = request.form.get('password')    
    session['username'] = username
    user = userDB.find_one({'username' : username})
    
    if user is None:
        userDB.insert_one({
            'author_name': author_name,
            'username': username,
            'password': password,
            'recipes_rated':[]
        })
        session['logged_in'] = True
        #flash('Welcome ' + user['author_name'] )
        return signin()
    else:
        session['logged_in'] = False
        flash('Username already exists, please try again.')
    return register()


@app.route('/signin')
def signin():
    if not session.get('logged_in'):
        return render_template('login.html', recipeCategory=recipeCategory.find(), page=1)
    else:
        return render_template('index.html', recipes=recipes.find().sort('date_time',pymongo.DESCENDING), 
        recipeCategory=recipeCategory.find(), page=1)


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username'].lower()
    password = request.form['password']
    session['username'] = username
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=30)
    user = userDB.find_one({'username' : username})
    
    if not user:
        session['logged_in'] = False
        flash('User ' + session['username'] + ' cannot be found on our system')
        return signin()
    if password == user['password']:
        session['logged_in'] = True
        flash('Welcome ' + user['author_name'].capitalize())
        return render_template('index.html', recipes=recipes.find(), 
        recipeCategory=recipeCategory.find(), author=user['author_name'])
    else:
        session['logged_in'] = False
        flash('Incorrect Password, please try again.')
    
    
@app.route('/logout')
def logout():
    session['logged_in'] = False
    return render_template('index.html', recipes=recipes.find().sort('date_time',pymongo.DESCENDING), 
    recipeCategory=recipeCategory.find(), page=1)  
    
    

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Browse Recipes                                                                                           #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    
@app.route('/browse_recipes/<recipe_category_name>/<page>', methods=['GET', 'POST'])
def browse_recipes(recipe_category_name, page):
    #Count the number of recipes in the Database
    all_recipes = recipes.find({'recipe_category_name': recipe_category_name}).sort([('date_time', pymongo.DESCENDING), ('_id', pymongo.ASCENDING)]) 
    count_recipes = all_recipes.count()
    
    #Variables for Pagination
    offset = (int(page) - 1) * 4
    limit = 4
    
    recipe_pages = recipes.find({'recipe_category_name': recipe_category_name}).sort([("date_time", pymongo.DESCENDING), 
                    ("_id", pymongo.ASCENDING)]).skip(offset).limit(limit)
    total_no_of_pages = int(math.ceil(count_recipes/limit))
   
    return render_template('browse_recipes.html',
    recipes=recipe_pages, recipeCategory=recipeCategory.find(),count_recipes=count_recipes, total_no_of_pages=total_no_of_pages, 
    page=page, recipe_category_name=recipe_category_name)
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Add Recipes                                                                                              #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#    

@app.route('/add_recipe', methods=['GET','POST'] )
def add_recipe():
    username=session.get('username')
    return render_template('add_recipe.html', recipes=recipes.find(), recipeCategory=recipeCategory.find(), 
            skillLevel=skillLevel.find(), allergens=allergens.find(), userDB = userDB.find(), page=1)

  
@app.route('/insert_recipe', methods=['GET','POST'])
def insert_recipe():
    username=session.get('username')
    user = userDB.find_one({'username' : username}) 
    recipe_tags = request.form.get('recipe_tags')
    recipe_tags_split = [x.strip() for x in recipe_tags.split(',')]
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
            'date_time': datetime.now(),
            'author_name': user['author_name'],
            'ratings':[
                    {'overall_ratings': 0.0,
                    'total_ratings': 0,
                    'no_of_ratings':0
                    }
                ],
            'recipe_tags': recipe_tags_split
        }   
    recipes.insert_one(complete_recipe)
    return redirect(url_for('my_recipes',page=1))
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Edit Recipes                                                                                             #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#    

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    return render_template('edit_recipe.html', recipeCategory=recipeCategory.find(), 
            allergens=allergens.find(), skillLevel=skillLevel.find(), page=1,
            recipes=recipes.find_one({'_id': ObjectId(recipe_id)}))
            
@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    recipe_tags = request.form.get('recipe_tags')
    recipe_tags_split = [x.strip() for x in recipe_tags.split(',')]
    recipes.update( {'_id': ObjectId(recipe_id)},
        { 
            '$set':{
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
            'recipe_tags': recipe_tags_split
            }
        })    
    return redirect(url_for('get_recipes'))        

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Delete Recipes                                                                                           #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#  


@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Users My Recipes Page                                                                                    #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#  

@app.route('/my_recipes/<page>', methods=['GET','POST'])
def my_recipes(page):
    username=session.get('username')
    user = userDB.find_one({'username' : username})
    author = user['author_name']
    
    #Count the number of recipes in the Database
    all_recipes = recipes.find({'author_name': author}).sort([('date_time', pymongo.DESCENDING), ('_id', pymongo.ASCENDING)]) 
    count_recipes = all_recipes.count()
    #Variables for Pagination
    offset = (int(page) - 1) * 4
    limit = 4
    total_no_of_pages = int(math.ceil(count_recipes/limit))
    recipe_pages = recipes.find({'author_name': author}).sort([("date_time", pymongo.DESCENDING), 
                    ("_id", pymongo.ASCENDING)]).skip(offset).limit(limit)
  
    return render_template('my_recipes.html',
    recipes=recipe_pages.sort('date_time',pymongo.DESCENDING), count_recipes=count_recipes, 
    total_no_of_pages=total_no_of_pages, page=page, author_name = author, recipeCategory=recipeCategory.find())

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Individual Recipe Page                                                                                   #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    
@app.route('/recipe_page/<recipe_id>', methods=['GET','POST'])
def recipe_page(recipe_id):
    username=session.get('username')
    user = userDB.find_one({'username' : username}) 

    recipe_rated_by_author = user['recipes_rated']
        
    return render_template('recipe.html', recipe=recipes.find_one({'_id': ObjectId(recipe_id)}), 
    recipeCategory=recipeCategory.find(), recipe_id = recipe_id, recipe_rated_by_author=recipe_rated_by_author, user=user, page=1)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Searching Keywords                                                                                       #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

@app.route('/search_keyword', methods=['POST'])
def receive_keyword():
    return redirect(url_for('search_keyword', keyword=request.form.get('keyword'), page=1)) 
    
    
@app.route('/search_keyword/<keyword>/<page>', methods=['GET','POST'])
def search_keyword(keyword, page):
    recipes.create_index([('recipe_name', pymongo.ASCENDING), 
        ('recipe_ingredients', pymongo.ASCENDING), 
        ('recipe_category_name', pymongo.ASCENDING)], unique=True)
    #Count the number of recipes in the Database
    all_recipes = recipes.find({'$text': {'$search': keyword}}).sort([('date_time', pymongo.DESCENDING), ('_id', pymongo.ASCENDING)]) 
    count_recipes = all_recipes.count()
    
    #Variables for Pagination
    offset = (int(page) - 1) * 4
    limit = 4
    total_no_of_pages = int(math.ceil(count_recipes/limit))
    
    recipe_pages = recipes.find({'$text': {'$search': keyword}}).sort([("date_time", pymongo.DESCENDING), 
                    ("_id", pymongo.ASCENDING)]).skip(offset).limit(limit)
                    
    return render_template('search_by_keyword.html', keyword=keyword, 
        search_results = recipe_pages.sort('date_time',pymongo.DESCENDING), 
        recipeCategory=recipeCategory.find(), count_recipes=count_recipes, 
        total_no_of_pages=total_no_of_pages, page=page)
        
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Ratings                                                                                                  #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# 
@app.route('/recipe_rating/<recipe_id>', methods=['POST'])
def recipe_rating(recipe_id):
    username=session.get('username')
    user = userDB.find_one({'username' : username}) 
    new_rating = request.form['new_rating']
    recipe = recipes.find_one({'_id': ObjectId(recipe_id)})

    for rating in recipe['ratings']:
        overall_rating = rating['overall_ratings']
        total_rating = rating['total_ratings']
        no_of_ratings = rating['no_of_ratings']
        #Calculation for figuring out weighted rating
        rating = (((int(overall_rating * total_rating) + int(new_rating)) / (int(total_rating)+1)))
        rating = (round(rating,1))
    
    recipes.update( {'_id': ObjectId(recipe_id)},
        {'$set':{
            'ratings': [
                {
                    'total_ratings': int(total_rating) + int(new_rating),
                    'overall_ratings': rating,
                    'no_of_ratings': no_of_ratings + 1
                }
            ]}
        })
        
    userDB.update({"username": username},
                {'$addToSet': 
                {'recipes_rated' : recipe_id}}) 
    return redirect(url_for('recipe_page', recipe_id = recipe_id))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Error Pages                                                                                              #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html',recipeCategory=recipeCategory.find(), page=1), 404

@app.errorhandler(405)
def method_not_allowed(error):
    return render_template('500.html',recipeCategory=recipeCategory.find(), page=1), 405
    
@app.errorhandler(500)
def something_wrong(error):
    return render_template('500.html',recipeCategory=recipeCategory.find(), page=1), 500


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Development/Production environment test for debug                                                        #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)