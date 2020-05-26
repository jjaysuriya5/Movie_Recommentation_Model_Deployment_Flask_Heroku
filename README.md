# Movie_Recommentation_Model_Deployment_Flask_Heroku

URL - https://jjmovierecommendation-api.herokuapp.com/ (Note : This is a trained on a limited hollywood movie data base, User can get 3 - 10 similar movie recommendation to the selected movies as per the user input )

The below step by step actions are performed to deploy the model

Model building
model.ipynb - This file contains the training model where cosine similarity is calculated on the input data and the model is saved as model.pkl file

------------------------------

Creating Application
main.py - This File consist of Flask application where the user is asked to input the required field and the corresponding output is obtained when clicking the submit button

------------------------------

Procfile
Procfile - This file contains the python server name and the flask application name

------------------------------

requirements.txt
requirements.txt - This file contains the packages which are required for this project

------------------------------

Heroku
Finally deploy the model using Heroku(PAAS) model bu connecting to this github repository
