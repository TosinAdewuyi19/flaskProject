from flask import render_template, request, redirect, url_for, session, flash
from . import listings_bp
from app.models.listing import create_listing, get_all_listings, get_listing_by_id
from bson.objectid import ObjectId

@listings_bp.route('/')
def view_listings():
    listings = get_all_listings()
    return render_template('listings.html', listings=listings)

@listings_bp.route('/<listing_id>')
def listing_detail(listing_id):
    listing = get_listing_by_id(listing_id)
    return render_template('listing_detail.html', listing=listing)

@listings_bp.route('/create', methods=['GET', 'POST'])
def create():
    if 'user_id' not in session:
        flash("You must be logged in to create a listing.")
        return redirect(url_for('auth.login'))

    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        start_price = request.form['start_price']
        image_url = request.form['image_url']
        seller_id = session['user_id']
        seller_name = session['username']

        create_listing(title, description, start_price, image_url, seller_id, seller_name)
        flash('Listing created.')
        return redirect(url_for('listings.view_listings'))

    return render_template('create_listing.html')
