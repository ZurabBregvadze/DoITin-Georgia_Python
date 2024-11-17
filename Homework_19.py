########################################
#Homework_19 Task_1
########################################
import json

# Define the Product class
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def to_dict(self):
        """Convert the Product object to a dictionary."""
        return {
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity
        }

    @staticmethod
    def from_dict(data):
        """Create a Product object from a dictionary."""
        return Product(name=data['name'], price=data['price'], quantity=data['quantity'])

# Serialization method
def serialize_products_to_file(products, filename):
    with open(filename, 'w') as file:
        json.dump([product.to_dict() for product in products], file, indent=4)

# Deserialization method
def deserialize_products_from_file(filename):
    with open(filename, 'r') as file:
        product_data = json.load(file)
        return [Product.from_dict(data) for data in product_data]

# Create several Product objects
product1 = Product('Laptop', 1200.50, 5)
product2 = Product('Smartphone', 750.00, 10)
product3 = Product('Headphones', 150.25, 20)

# Add them to a list
products = [product1, product2, product3]

# Serialize the products to a JSON file
serialize_products_to_file(products, 'products.json')

# Deserialize the products from the JSON file
loaded_products = deserialize_products_from_file('products.json')

# Print all product information
for product in loaded_products:
    print(f"Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}")

############################################
