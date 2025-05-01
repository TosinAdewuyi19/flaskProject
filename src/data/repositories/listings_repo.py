from bson.objectid import ObjectId
from src.extensions import mongo

class ProductRepository:
    def find_all(self):
        return list(mongo.db.products.find())

    def insert_product(self, product_data):
        return mongo.db.products.insert_one(product_data)

    def find_by_id(self, product_id):
        return mongo.db.products.find_one({"_id": product_id})


    def update_product(self, product_id):
        return mongo.db.products.update_one({"_id": product_id})

    def remove_product(self, product_id):
        return mongo.db.products.delete_one({"_id": product_id})