from flask import Flask, render_template
from flask_pymongo import PyMongo
from flask_login import LoginManager, login_user, logout_user, login_required
from dto import UserDTO, AuctionDTO
import jwt
import datetime
from flask import Flask, request, jsonify
from functools import wraps

import cloudinary
import cloudinary.uploader
import cloudinary.api

from flask import request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash

from src.data.models.user import User

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/auction_db"
app.secret_key = "your_secret_key"
app.config['SECRET_KEY'] = 'your_secret_key'
mongo = PyMongo(app)
login_manager = LoginManager()
login_manager.init_app(app)
cloudinary.config(
    cloud_name="dkgbqdjxk",
    api_key="895326556966715",
    api_secret="VmUJEFVBD0OQqjokbd3ruu_s88M",
)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/create_auction', methods=['POST'])
@login_required
def create_auction():
    # Sample data for auction creation
    auction_dto = AuctionDTO(
        title="Sample Auction",
        description="This is a sample auction item.",
        starting_bid=100,
        current_bid=100,
        end_time="2025-05-01T15:00:00Z"
    )
    # Insert auction into MongoDB
    mongo.db.auctions.insert_one(auction_dto.__dict__)
    return "Auction created!"

from flask import request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user_type = request.form['user_type']

        # Hash the password
        hashed_password = generate_password_hash(password, method='sha256')

        # Store user in MongoDB
        mongo.db.users.insert_one({
            'username': username,
            'email': email,
            'password': hashed_password,
            'user_type': user_type
        })
        flash("Registration successful! You can now log in.")
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = mongo.db.users.find_one({'username': username})

        if user and check_password_hash(user['password'], password):
            login_user(User(username=user['username'], email=user['email'], password=user['password']))
            return redirect(url_for('home'))
        flash("Invalid username or password.")
    return render_template('login.html')

@login_manager.user_loader
def load_user(user_id):
    user_data = mongo.db.users.find_one({'username': user_id})
    return User(username=user_data['username'],
                email=user_data['email'],
                password=user_data['password']
                user_type=user_data['user_type']
            ) if user_data else None


@app.route('/bid/<auction_id>', methods=['POST'])
@login_required
def bid(auction_id):
    auction = mongo.db.auctions.find_one({'_id': auction_id})
    if auction:
        bid_amount = float(request.form['bid_amount'])
        if bid_amount > auction['current_bid']:
            # Update the auction with the new bid
            mongo.db.auctions.update_one(
                {'_id': auction_id},
                {
                    '$set': {
                        'current_bid': bid_amount,
                        'highest_bidder': current_user.username
                    }
                }
            )
            return "Bid placed successfully!"
        else:
            return "Bid must be higher than the current bid."
    return "Auction not found."


if __name__ == '__main__':
    app.run(debug=True)
