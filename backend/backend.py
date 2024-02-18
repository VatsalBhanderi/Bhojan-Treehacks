from flask import Flask, request, jsonify, render_template
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# PostgreSQL Configuration
# app.config['SQLALCHEMY_DATABASE_URI'] = ''
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

class User():
    # id = db.Column(db.Integer, primary_key=True)
    # username = db.Column(db.String(50), unique=True, nullable=False)
    # password = db.Column(db.String(50), nullable=False)
    id=1
    username="username"
    password="password"

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# @app.route('/')
# def index():
#     return render_template('login.html')

class SubmitMeal():
    isFoodGood = "Yes"
    calories = 200
    foodMood = "Breakfast"

@app.route('/getRecommendations', methods=['GET'])
def getRecommendations():
    if request.method == 'GET':
        try:
            data = request.get_json()
            mealTime = request.args.get('mealTime', type=str)
            calorieLeft = 200 #take this calorie from mongo
            return jsonify({"mealRec": "150gm Chia Seeds, 5 strawberries", "calories":150})
            
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
            return jsonify(data), 201
            # return jsonify({'message': 'File uploaded successfully', 'filename': filename}), 201

        except:
            return jsonify({"message": "Error: {}".format(str(e))}, 500)


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
