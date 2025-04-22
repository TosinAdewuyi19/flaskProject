from bson.objectid import ObjectId
from src.app import mongo

class ProductRepository:
    def __init__(self):
        self.collection = mongo.db.products

    def insert_product(self, product_data):
        result = self.collection.insert_one(product_data)
        product_data["_id"] = str(result.inserted_id)
        return product_data

    def find_all(self):
        products = list(self.collection.find())
        for p in products:
            p["_id"] = str(p["_id"])
        return products

    def find_by_id(self, product_id):
        try:
            product = self.collection.find_one({"_id": ObjectId(product_id)})
            if product:
                product["_id"] = str(product["_id"])
            return product
        except Exception:
            return None
