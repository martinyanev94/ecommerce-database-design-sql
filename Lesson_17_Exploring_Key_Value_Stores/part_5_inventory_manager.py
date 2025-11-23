class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, product_id, quantity):
        self.items[product_id] = self.items.get(product_id, 0) + quantity

    def get_item_quantity(self, product_id):
        return self.items.get(product_id, 0)

inventory = Inventory()
inventory.add_item('product_ABC', 100)
print(inventory.get_item_quantity('product_ABC'))
