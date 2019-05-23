Online Cookbook - Data Centric Development Milestone Project
======================================
**Online Cookbook Project - Milestone Project 3 for the Code Institute**

This [project](https://deevdz-milestone-3.herokuapp.com/) was designed and developed to be an online recipe cookbook for users. Users can browse and rate recipes listed. Users also have the option to create their own account where they can add, edit and delete their own recipes.

The project needs to be able to demonstrate the use of CRUD functions:
```
1.  Create something
2.  Read something
3.  Update something
4.  Delete a something
````


Database Schema
-----------------------------------------
[MongoDB](https://www.mongodb.com/) was used to create the database for this website and it is hosted by [Atlas](https://www.mongodb.com/cloud/atlas).

Some of the queries were easy to forsee while some evolved over the development of the site. Original plans for the database schema can be [found here](https://github.com/deevdz/milestone-project-3/blob/master/planning/Online%20Cookbook%20Project%20-%20Initial%20Thoughts.pdf).

The final database schema consists of five collections which include recipes, users, allergens, recipeCategory and skillLevel. 

Final database schema diagrams can be found in the folder [Database Schema](https://github.com/deevdz/milestone-project-3/blob/master/planning/database_schema).

UX
-----------------------------------------
Documentation for the initial planning process can be [found here](https://github.com/deevdz/milestone-project-3/blob/master/planning/Online%20Cookbook%20Project%20-%20Initial%20Thoughts.pdf).

The wireframes for this site were generated using Adobe Illustrator. Wireframes for the site can be found in the folder [planning > wireframes](https://github.com/deevdz/milestone-project-3/tree/master/planning/wireframes)

After browsing through food blogs and recipe archives online the decision was made to use earthy tones. Colour Palette and final logo design can be [found here]().

Research was carried out on complimentary fonts and Libre Baskerville and Monsterrat were chosen for the site.

###### User Stories
  * As a user - I am immediately aware what the nature of the site is and its purpose
  * As a user - I can navigate through the recipes by various means i.e. Feature Slider, Navigation dropdown
  * As a user - I can browse the site without being a logged in user
  * As a user - I can create a user profile, and log in and out
  * As a user - I can add, edit and delete my own recipes through my user account
  * As a user - I can rate a recipe once, as long as I am logged in user
  * As a user - I receive an error message if I am unable to login or register
  * As a user - I am able to access the site on mobile or tablet and have a similar experience as a desktop device
  * As a user - I can search for a recipe to filter my results
  * As a user - I can filter recipes based on recipe tags
  * As a user - I am able to see the total number of recipes in a category
  * As a user - I am able to see the details of the recipe
  * As a user - I am prompted to sign up or add a recipe if a category is empty
  * As a user - I am able to page through categories if there are more than 6 results.


Features
-----------------------------------------
###### Existing Features
The site can be used as a guest or as a logged in user, however some features are only available to logged in users.

Any visitor to the site can view the featured recipes in the homepage slider, use the navigation to filter through recipe categories, search for specific keywords and use the tags to filter recipes. The search function at present only returns results with the keyword appearing in either recipe name, ingredients or recipe category.

All visitors can browse all recipes. Results are returned in order of newest recipe added to the site. From the results a specific recipe page can be viewed. Six recipes are displayed per page. Where a page has more than six recipes to display pagination options appear. Visitors are informed as to how many recipes are in each category and how many pages of results there are.

Visitors have the option of create an account. Information required to create an account is Full Name, Username (which must be unique) and password. This information is stored in the users collection. The Full Name and Username are stored as plain text but the password is stored in a hashed format.

When a visitor has created an account and logged in they are given the option to Add a recipe to the system, Edit their recipes, Delete their recipe from the system and rate any recipe on the site. Users can view recipes they have added to the site in the My Recipes section.

Adding a new recipe will create a new document in the recipe collection using the required fields.. The user has the option to feature this recipe on the homepage slider and adding tags to the recipe to allow visitors to easily filter through the recipes on the site.

A user has the option to edit or delete a recipe that they have added to the site only. Editing the recipe allows the user to update/or add to the existing recipe information. Deleting the recipe permanently removes the recipe from the system.



###### Future Features

Images - could be improved by letting the user to upload an image from their computer. Also a gallery of images for a dish would be a nice feature.

Reviews/Comments - Expand the ratings system to allow users to leave a detailed review/comment about a recipe.

User accounts - Passwords are currently stored in a hash format but it is an important requirement to make sure that user logins are made more secure.

User Dashboard - A dashboard where the user could update their details including password.

Following - A feature for users to able to follow other users on the site and receive updates on their dashboard when users add new recipes.

Undo Delete - Provide users with an archive of deleted recipes with the option to add the recipe back onto the system


Technologies Used
-----------------------------------------
The website is designed using following technologies:

   HTML  
   CSS  
   JavaScript  
   [Python](https://www.python.org/)  
   [Flask](http://flask.pocoo.org/)  
   [Mongodb](https://www.mongodb.com/)  
   [Jquery](https://code.jquery.com/jquery-3.2.1.js)  
   [Font Awesome library](https://fontawesome.com/)  
   [Materializecss 0.100.2](http://archives.materializecss.com/0.100.2/)  
   [Google Fonts](https://fonts.google.com/)  
   [UIkit](https://getuikit.com/)


Testing
-----------------------------------------
**Responsiveness Testing:**

Developer Tools, android mobile phone and android tablet were used to test the appearance of website on mobile/tablet screen size.  
   
All tests were carried out manually and the testing process was as follows:

**Homepage**

**Category Pages**

**User Account**

###### Register Page
###### Login Page
###### Add Recipe
###### Edit Recipe
###### Delete Recipe
###### Logout

**Recipe Page**

**Search by Keyword**

**Serach by Tag**

**Error Pages**



Deployment
-----------------------------------------
Deployment and source control was carried out via GitHub and Heroku. The repository location is as follows:[https://github.com/deevdz/milestone-project-3](https://github.com/deevdz/milestone-project-3)

Heroku App Location is as follows [https://deevdz-milestone-3.herokuapp.com/](https://deevdz-milestone-3.herokuapp.com/)

Following steps were taken to deploy the website:
1. Database and Tables were created in an Atlas MongoDB account
2. Project workspace was created in Cloud 9. In this workspace: Flask was installed - `sudo pip install flask`.
3. Setup app.py file and imported flask and os - `from flask import Flask. import os`
4. Created an instance of flask - `app = flask(__name__)`
5. Tested the connection as proof of concept. `CLI - show collections` (prove connection)
6. Inside the app run() function set the host, ip and debug=true
7. Create a new Heroku App - unique name and EU Server
8. In cloud 9 login to Heroku through CLI to confirm existance of app. `CLI: heroku login. CLI: heroku apps`.
9. Create a git repository in cloud9. CLI: git init. `CLI: git add . CLI: git commit -m "Initial Commit"`
10. Connect cloud9 to Heroku. Use code found on Heroku. `CLI - $heroku git remote -a deevdz-milestone-3`
11. Create requirements.txt file - `CLI: sudo pip3 freeze --local > requirements.txt`
12. Create Procfile - `echo web:python app.py>Procfile`
13. Add and Commit to Git Repository
14. Push to Heroku using code supplied by Heroku
15. `CLI - heroku ps:scale web=1` Command to tell Heroku to run the app
16. Login to Heroku to add config variables including IP, Port, Mongo_DB and Mongo_URI
17. Get Flask to talk to MongoDB - `CLI: sudo pip3 install flask-pymongo` `CLI: sudo pip3 install dnspython`
18. Add extra libraries to app.py - `from flask_pymongo import Pymongo` `from bson.objectid import ObjectID`
19. Add DB connection code to app.py - edit bashrc file to keep details private.
20. Test connection to DB again to confirm it's working
21. Confirm that the cloud9 runner is set to python 3
22. Connect GitHub repository to Heroku using code provided by heroku and github.

Credits
-----------------------------------------
**Content**

All site recipes and images are sourced from [BBC Food](https://www.bbc.com/food/recipes) and [Pinterest](https://www.pinterest.ie/).


**Code References**

  * [Full screen search overlay](https://codepen.io/thisisabhinay/pen/MypbGK)  
  * [Formula for calculating user ratings](https://stackoverflow.com/questions/10196579/algorithm-used-to-calculate-5-star-ratings/38378697)  
  * [Issues with for loops](https://stackoverflow.com/questions/34877236/for-loop-not-working-in-jinja-flask)
  * [Star Ratings CSS](https://codepen.io/Bluetidepro/pen/GkpEa)
  * [Share Links](https://sharingbuttons.io/)
  * [Splitting Tag List to create array](https://pynative.com/python-accept-list-input-from-user/)
  * [Taking input Using Materialize Chips](https://stackoverflow.com/questions/42253115/symfony-best-practice-using-materialize-css-chips-with-symfony-forms?rq=1)
  * [Information on Logging In](https://pythonspot.com/login-authentication-with-flask/)
  * [Information on how to keep a session live](https://stackoverflow.com/questions/18662558/flask-login-session-times-out-too-soon)
  * [Passing Username through Session](https://stackoverflow.com/questions/27611216/how-to-pass-a-variable-between-flask-pages/27611281#27611281)
  * [Pagination](https://www.youtube.com/watch?v=Lnt6JqtzM7I)
  * [Hashing Passwords](https://www.youtube.com/watch?v=jJ4awOToB6k)

**Acknowledgements**

I would like to thank my tutors and mentor at the Code Institute for all their help and support during the development of this project.

**Contact**

Created by [Deirdre van der Zee](mailto:deirdrevanderzee@gmail.com).