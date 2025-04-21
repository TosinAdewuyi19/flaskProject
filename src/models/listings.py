from datetime import datetime
from app.extensions import mongo
from bson.objectid import ObjectId

def create_listing(title, description, start_price, image_url, seller_id, seller_name):
    listing = {
        'title': title,
        'description': description,
        'start_price': float(start_price),
        'image_url': image_url,
        'seller_id': seller_id,
        'seller_name': seller_name,
        'created_at': datetime.utcnow(),
        'bids': []  # list of bids
    }
    return mongo.db.listings.insert_one(listing)

def get_all_listings():
    return mongo.db.listings.find()

def get_listing_by_id(listing_id):
    return mongo.db.listings.find_one({'_id': ObjectId(listing_id)})
