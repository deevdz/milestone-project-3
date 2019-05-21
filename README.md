Online Cookbook - Data Centric Development Milestone Project
======================================
**Online Cookbook Project - Milestone Project 3 for the Code Institute**

This project was designed and developed to be an online recipe cookbook for users. Users can browse and rate recipes listed. Users also have the option to create their own account where they can add, edit and delete their own recipes.

The project needs to be able to demonstrate the use of CRUD functions:
```
1.  Create something
2.  Read something
3.  Update something
4.  Delete a something
````


Database Schema
-----------------------------------------
[MongoDB](https://www.mongodb.com/) was used to create the database for this website and it was hosted by [Atlas](https://www.mongodb.com/cloud/atlas).

Some of the queries were easy to forsee while some evolved over the development of the site.

The final database schema consists of five collections which include recipes, users, allergens, recipeCategory and skillLevel. 

Final database schema diagram can be found in the folder [Database Schema](/planning/database_schema).


UX
-----------------------------------------
Documentation for the initial planning process can be [found here](/planning/Online Cookbook Project - Initial Thoughts.pdf).

Features
-----------------------------------------
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
Deployment
-----------------------------------------
Deployment and source control was carried out via GitHub and Heroku. The repository location is as follows:[https://github.com/deevdz/milestone-project-3](https://github.com/deevdz/milestone-project-3)

Heroku App Location is as follows [https://deevdz-milestone-3.herokuapp.com/](https://deevdz-milestone-3.herokuapp.com/)

Following steps were taken to deploy the website:
1. Database and Tables were created in an Atlas MongoDB account
2. Project workspace was created in Cloud 9. In this workspace: Flask was installed -  MongoDB client for Atlas was installed - 
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
