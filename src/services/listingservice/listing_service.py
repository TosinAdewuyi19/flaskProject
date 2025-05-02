import cloudinary.uploader
from flask import request, render_template

from src.extensions import mongo


@app.route('/create_auction', methods=['POST'])
def create_auction():
    title = request.form['title']
    description = request.form['description']
    starting_bid = float(request.form['starting_bid'])
    image = request.files['image']

    upload_result = cloudinary.uploader.upload_image()

    auction_dto = AuctionDTO(
        title=title,
        description=description,
        starting_bid=starting_bid,
        current_bid=starting_bid,
        end_time="2025-05-01T15:00:00Z"  # Set a default end time
    )

    mongo.db.auctions.insert_one(auction_dto.__dict__)
    return "Auction created!"

@app.route('/auctions')
def view_auctions():
    auctions = mongo.db.auctions.find()
    return render_template('auctions.html', auctions=auctions)

