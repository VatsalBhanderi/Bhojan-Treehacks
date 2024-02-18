from flask import Flask, request, jsonify, render_template
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import requests
import json
import os
import predictionguard as pg


url = "https://us-west-2.aws.data.mongodb-api.com/app/data-zfksj/endpoint/data/v1/action/findOne"
mongoUri = "mongodb+srv://ashutoshpatil610:mBUQ728xrpss5T8G@bhojan.hiqnkos.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

mongo_client = MongoClient(mongoUri)
db = mongo_client['daily']  # Use your database name
collection = db['Bhojan']  # Use your collection name

# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# PostgreSQL Configuration
# app.config['SQLALCHEMY_DATABASE_URI'] = ''
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

class User():
    

class UserMeals():
    # id = db.Column(db.Integer, primary_key=True)
    # username = db.Column(db.String(50), unique=True, nullable=False)
    # password = db.Column(db.String(50), nullable=False)
    date=""
    mealTime=""
    calorieIntake=100
    mealVal=""

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# @app.route('/')
# def index():
#     return render_template('login.html')

class SubmitMeal():
    isFoodGood = "Yes"
    calories = 200
    foodMood = "Breakfast"


@app.route('/initData', methods=['GET'])
def getInitData():
    if request.method == 'GET':
        try:
            db.collection.find()

@app.route('/getRecommendations', methods=['GET'])
def getRecommendations():
    if request.method == 'GET':
        try:
            mealTime = request.args.get('mealTime', type=str)
            # calorieLeft = 200 #take this calorie from mongo

            # Call LLM model for the recommendation, using the mealtime and calories left
            #############################################################################
            return extractBurnedCalories(mealTime)
            
        except:
            return jsonify({"message": "Error: {}".format(str(e))}, 500)


@app.route('/submitMeal', methods=['POST'])
def submitMeal():
    if request.method == 'POST':
        try:
            if 'file' not in request.files:
                return jsonify({'message': 'No file part in the request'}), 400
            file = request.files['file']
            
            # If the user does not select a file, the browser submits an
            # empty file without a filename.
            if file.filename == '':
                return jsonify({'message': 'No selected file'}), 400
            
            if file:
                # You can save the file to the server
                filename = file.filename
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                
            #need to write code to evaluate the image
            #########################################

            submitMeal = SubmitMeal()
            isFoodGood = submitMeal.isFoodGood
            calories = submitMeal.calories
            foodMood = submitMeal.foodMood

            data = {"isFoodGood": isFoodGood, "calories": calories, "foodMood": foodMood}
            collection.insert_one
            return jsonify(data), 201
            # return jsonify({'message': 'File uploaded successfully', 'filename': filename}), 201

        except:
            return jsonify({"message": "Error: {}".format(str(e))}, 500)

@app.route('/acceptMeal', methods=['POST'])
def acceptMeal():
    if request.method == 'POST':
        data = request.get_json
        if data['acceptMeal']:
            if last_meal.isFoodGood == 'No':
                return jsonify({'message': 'Thats fine! You deserve a treat "sometimes".'}), 201

            elif last_meal.isFoodGood == 'Yes':
                return jsonify({'message': 'Congrats for choosing a healthy option'}), 201

@app.route('/getExercises', methods=['POST'])
def getExercises():
    if request.method == 'GET':
        calories = 300
        # send request to LLM to get exercises to burn X calories
        return jsonify({'message':'A,B,C'}), 201

def extractBurnedCalories(mealTime):

    payload = json.dumps({
    "collection": "daily",
    "database": "Bhojan",
    "dataSource": "Bhojan",
    "projection": {
        "calories_data": 1
    }})

    headers = {
      'Content-Type': 'application/json',
      'Access-Control-Request-Headers': '*',
      'api-key': 'UHEJiHgC2o4J7F5yojfKVIprkWvL0nQTe3C2skBufqPavsB8XjxXMJ1kWTc0b8fV',
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


    data = json.loads(response.text)
    net_activity_calories = data['document']['calories_data']['total_burned_calories']

    # Set your Prediction Guard token as an environmental variable.
    os.environ["PREDICTIONGUARD_TOKEN"] = "q1VuOjnffJ3NO2oFN8Q9m8vghYc84ld13jaqdF7E"

    HEIGHT = 175  # in cms
    WEIGHT = 75  # in Kgs
    EXERCISE = net_activity_calories
    CUISINE = "Indian"
    MEAL_TIME = mealTime

    totalCaloriesToGO = 500

    bmr = data['document']['calories_data']['BMR_calories']

    if MEAL_TIME == "Breakfast": 
        bmr = bmr*0.22

    elif MEAL_TIME == "Lunch": 
        bmr = bmr*0.31

    elif MEAL_TIME == "Dinner": 
        bmr = bmr*0.35

    messages = [
        {
            "role": "system", 
            "content": """You are a Healthy meal recommender agent that takes in some parameters from the user and returns data in JSON in this format:
            {
          "mealTime": f"{MEAL_TIME}".format(MEAL_TIME),
          "foods": [
            {
              "name": "Oatmeal",
              "calories": {bmr},
              "quantity": "1 cup"
            }
          ]
        }
      ]
    } Only return the JSON, nothing else.""",
        },
        {
            "role": "user",
            "content": f"Meal time: {MEAL_TIME}, Height: {HEIGHT} cm, Weight: {WEIGHT} Kg, Workout calories burnt: {EXERCISE}, Cuisine preference: {CUISINE}.".format(HEIGHT, WEIGHT, EXERCISE, CUISINE)
        }
    ]

    result = pg.Chat.create(
        model="Nous-Hermes-2-SOLAR-10.7B",
        messages=messages
    )

    print(json.dumps(
        result,
        sort_keys=True,
        indent=4,
        separators=(',', ': ')
    ))

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        try:
            # Assuming your front-end sends data as JSON
            data = request.get_json()

            # Get username and password from the request
            username = data.get('username')
            password = data.get('password')

            # Query the database for the user
            # user = User.query.filter_by(username=username).first()
            user = User()
            if user and user.password == password:
                # Successful login
                return jsonify({"message": "Login successful"})
            else:
                # Invalid credentials
                return jsonify({"message": "Invalid credentials"}), 401

        except Exception as e:
            return jsonify({"message": "Error: {}".format(str(e))}, 500)


if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)
