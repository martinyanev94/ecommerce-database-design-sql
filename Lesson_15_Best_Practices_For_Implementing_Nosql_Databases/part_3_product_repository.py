class ProductRepository:
    def __init__(self, db_connection):
        self.collection = db_connection['products']

    def get_product(self, product_id):
        return self.collection.find_one({"product_id": product_id})

    def add_product(self, product):
        self.collection.insert_one(product)

# Usage
product_repo = ProductRepository(db)
product_details = product_repo.get_product("prod-12345")
