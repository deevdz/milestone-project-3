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
```


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

##### User Stories
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
##### Existing Features

The site can be used as a guest or as a logged in user, however some features are only available to logged in users.

Any visitor to the site can view the featured recipes in the homepage slider, use the navigation to filter through recipe categories, search for specific keywords and use the tags to filter recipes. The search function at present only returns results with the keyword appearing in either recipe name, ingredients or recipe category.

All visitors can browse all recipes. Results are returned in order of newest recipe added to the site. From the results a specific recipe page can be viewed. Six recipes are displayed per page. Where a page has more than six recipes to display pagination options appear. Visitors are informed as to how many recipes are in each category and how many pages of results there are.

Visitors have the option of create an account. Information required to create an account is Full Name, Username (which must be unique) and password. This information is stored in the users collection. The Full Name and Username are stored as plain text but the password is stored in a hashed format.

When a visitor has created an account and logged in they are given the option to Add a recipe to the system, Edit their recipes, Delete their recipe from the system and rate any recipe on the site. Users can view recipes they have added to the site in the My Recipes section.

Adding a new recipe will create a new document in the recipe collection using the required fields.. The user has the option to feature this recipe on the homepage slider and adding tags to the recipe to allow visitors to easily filter through the recipes on the site.

A user has the option to edit or delete a recipe that they have added to the site only. Editing the recipe allows the user to update/or add to the existing recipe information. Deleting the recipe permanently removes the recipe from the system.

Any recipe can be rated once by a logged in user. Users can choose between a rating of 1 to 5. Calculating the weighted value of the recipe rating was based on the [following formula](https://stackoverflow.com/questions/10196579/algorithm-used-to-calculate-5-star-ratings/38378697). Each rating is accounted for and the visitor is informed of the user rating and how many times this recipe has been rated.

The site features custom error pages for both 404 and 500 errors.

##### Future Features

**Images** - could be improved by letting the user to upload an image from their computer. Also a gallery of images for a dish would be a nice feature.

**Reviews/Comments** - Expand the ratings system to allow users to leave a detailed review/comment about a recipe.

**User accounts** - Passwords are currently stored in a hash format but it is an important requirement to make sure that user logins are made more secure.

**User Dashboard** - A dashboard where the user could update their details including password.

**Following** - A feature for users to able to follow other users on the site and receive updates on their dashboard when users add new recipes.

**Undo Delete** - Provide users with an archive of deleted recipes with the option to add the recipe back onto the system


Technologies Used
-----------------------------------------
The website is designed using following technologies:

  * HTML
  * CSS
  * JavaScript
  * [Python](https://www.python.org/)
  * [Flask](http://flask.pocoo.org/)
  * [Mongodb](https://www.mongodb.com/)
  * [Jquery](https://code.jquery.com/jquery-3.2.1.js)
  * [Font Awesome library](https://fontawesome.com/)
  * [Materializecss 0.100.2](http://archives.materializecss.com/0.100.2/)
  * [Google Fonts](https://fonts.google.com/)
  * [UIkit](https://getuikit.com/)


Testing
-----------------------------------------
**Automated Testing:**

Using pythons built-in [Unit Test Framework](https://docs.python.org/3/library/unittest.html), automated tests were carried out on routes and forms. A testcase was created by subclassing unittest.TestCase.

The [test suite](https://github.com/deevdz/milestone-project-3/blob/master/tests/tests.py) was started with a Setup() and ended with a TearDown() in accordance with the [Ordering Test Code](https://docs.python.org/3/library/unittest.html#organizing-test-code) suggested in the Unit Test Framework.

Automated tests were setup and asserted that all routes behaved as expected i.e 200 - route ok, 404 - route not found.

Tests were established to verify writing to the database and removing from the database i.e. Adding a user to the database and then removing the user and deleting a recipe from the database.

**Responsiveness Testing:**

Developer Tools, android mobile phone and android tablet were used to test the appearance of website on mobile/tablet screen size.  
   
**User Testing:**

All tests were carried out manually and the testing process was as follows:

**Homepage**
 + Click on logo or Home and verify that home page appears.
 + Click on Recipes dropdown - verify all categories are loading as options with links to the correct categories
 + If visitor is not logged in “Login” should be displayed in the navigation and clicking this link will bring you to the login page.
 + If visitor is logged in the navigation should read “Account” with dropdown links to Add recipe, My Recipes and Logout. Also should display the correct Username.
 + Search Button - click to open full screen overlay search box.
 + Ensure slider displaying correct recipes, links to recipes going to correct pages and arrows on slider working
 + “You may also be interested in” should display the four newest recipes added to the site with links to the individual recipes.
 + Clicking on the “Browse All Recipes” button brings you to the All recipes page.
 + Confirmed that the right side category links link to the correct pages
 + Verify that 20 tags are being loaded on the right side of the page with links going to search results of that tag.
 + Confirmed that the social links in the footer open in a new browser window and go to the correct links

**Category Pages**
 + Click through to each category page and confirmed that the correct header and recipes were displaying
 + Confirmed that if there were no recipes to display user is prompted to either log in and add a recipe or if already logged in to just add a recipe.
 + Confirmed that if less than six recipes were displayed that the pagination is hidden
 + Confirmed that the pagination is working correctly when there are more than 6 recipes to display
 + Verified that clicking on a recipe brings the user to the correct detailed recipe page.

**User Account**

###### Register Page
+ Confirmed that clicking on the sign up link brings the user to the registration page
+ All fields are required on the registration form
+ Tested registering successfully and was returned to the homepage as a logged in user with a welcome message.
+ Confirmed that username must be unique - if user tries to register with a username that already exists the following message appears "Username already exists, please try again."

###### Login Page
+ Confirm that the login link brings the user to the login page
+ If user enters an incorrect username then they will receive the following message "User *** cannot be found on our system. Please try again. "
+ If user enters a correct username but an incorrect password they will receive the following message "Incorrect Password, please try again."
+ If the user enters the correct login details they are brought to the homepage with a welcome message. Navigation changes from Login to Account dropdown with option to Add Recipe, View Recipes and Logout.

###### Add Recipe
+ User can only add a recipe if they are logged in. If user finds this page without being logged in they are prompted to do so.
+ Confirmed that all fields are required fields except for allergens.
+ Confirmed that recipe is added correctly to the system by seeing it displayed on the site.

###### Edit Recipe
+ User can only edit a recipe if they are logged in and they have added the recipe to the site. If user finds this page without being logged in they are prompted to do so. 
+ Confirmed that this page is working by clicking on the edit button and seeing the results that are returned.
+ Verify that the edit recipe is working correctly by making a change to the recipe and updating it.

###### Delete Recipe
+ On the Recipe page, verified that the delete button is only displayed to the logged in user that added that recipe to the system.
+ Confirmed that the recipe is deleted from the system by checking the Database.

###### My Recipes
+ Confirm that only recipes added by the user are displayed here
+ Confirm that the user can only see this page once logged in.
+ Confirm that pagination is displayed when user has more than 6 recipes added.

###### Logout
+ Verified that the user is returned to the homepage and logged out of the system.

**Recipe Page**
+ Confirm that clicking on a recipe link, ie through the slider, category cards brings the user to a detailed version of the recipe.
+ Verified that the correct details are being displayed in the correct positions for each recipe.
+ Checked that the social share links are working correctly.
+ Confirmed that the user rating is displaying correctly.
+ User must be logged in to rate a recipe. User is prompted to login if they are not. If the user is logged in they are prompted to rate the recipe. If the user has previously rated the recipe they are not given the option to rate it again.
+ Verified that the recipe tags are working correctly. 

**Search by Keyword**
+ Enter a value into the search form and confirm that the correct results are returned with paginaition where applicable.
+ Confirmed Search box is a required field.
+ Confirmed that clicking anywhere on the screen closes the search overlay.

**Serach by Tag**
+ Click on a tag link and confirm that the correct results are returned for the tag clicked and results are displayed with pagination where applicable.

**Error Pages**
 + Try going to [http://deevdz-milestone-3.herokuapp.com/test](http://deevdz-milestone-3.herokuapp.com/test) and observe the custom 404 error.
 + Confirmed that there was a working link back to the homepage and that links in the navigation are working on the 404 error page.

**Issues Found & Fixes Implemented**
- Issue: Homepage slider area would display even if no recipe had the featured recipe switched on. Fix: Count the number of recipes that have the feature switched on if it is less than one then hide the area.
- Issue: Duplicates of the tags were displaying and the same tags were displaying each time the page loaded. Fix: Used the distinct function solve this issue and then used the shuffle function to randomise the order.
- Issue: Could not get the links to work on the materialize Homepage slider. Fix: Now using the slider provided by UIKit as it had the functionality required.
- Issue: Recipes being displayed on the wrong author page. Fix: Made the recipes group by Username rather than Author Name as username has to be unique.
- Issue: Being logged out of the session too quickly. Fix: Found a fix to the issue [here](https://stackoverflow.com/questions/18662558/flask-login-session-times-out-too-soon)
- Issue: Adding tags through a form using Materialize chips. Fix: Found a fix here as how to bind the chips to a hidden input field [here](https://stackoverflow.com/questions/42253115/symfony-best-practice-using-materialize-css-chips-with-symfony-forms?rq=1)
- Issue: Javascript error from the code used to bind the materialize chips to the hidden input field. Fix: Check the page to see if the class exists then execute the code otherwise ignore it. 

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
23. Set Debug to False

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