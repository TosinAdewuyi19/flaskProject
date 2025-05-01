from flask import Flask, render_template
from flask_pymongo import PyMongo
from flask_login import LoginManager

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/auction_db"
app.secret_key = "your_secret_key"  # Change this to a random secret key
mongo = PyMongo(app)
login_manager = LoginManager(app)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
