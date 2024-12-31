class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def display_info(self):
        print(f"Product: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Quantity Available: {self.quantity}")
        print("-" * 40)

    def update_quantity(self, quantity_sold_or_restocked):
        self.quantity += quantity_sold_or_restocked
        action = "restocked" if quantity_sold_or_restocked > 0 else "sold"
        print(f"{abs(quantity_sold_or_restocked)} units of '{self.name}' have been {action}.")
    
    def calculate_value(self):
        return self.price * self.quantity

class Inventory:
    def __init__(self):
        self.products = []
    
    def add_product(self, name, price, quantity):
        new_product = Product(name, price, quantity)
        self.products.append(new_product)
        print(f"Product '{name}' added to inventory.")
    
    def display_inventory(self):
        if not self.products:
            print("No products in the inventory.")
            return
        for product in self.products:
            product.display_info()
    
    def total_inventory_value(self):
        total_value = sum(product.calculate_value() for product in self.products)
        print(f"Total Inventory Value: ${total_value:.2f}")
        
# Create an inventory system
store_inventory = Inventory()

# Add products to the inventory
store_inventory.add_product("Laptop", 1200.00, 10)
store_inventory.add_product("Smartphone", 700.00, 25)
store_inventory.add_product("Headphones", 150.00, 50)

# Display all products in the inventory
print("\nDisplaying all products in the inventory:")
store_inventory.display_inventory()

# Update the quantity of a product (sold or restocked)
print("\nUpdating quantities:")
store_inventory.products[0].update_quantity(-2)  # Sold 2 Laptops
store_inventory.products[1].update_quantity(10)  # Restocked 10 Smartphones

# Display the updated inventory
print("\nDisplaying updated inventory:")
store_inventory.display_inventory()

# Calculate and display the total value of the inventory
store_inventory.total_inventory_value()
