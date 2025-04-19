from flask import Blueprint, jsonify, request
from services.auction_services import AuctionServices

auction_bp = Blueprint('auction', __name__)
auction_services = AuctionServices()