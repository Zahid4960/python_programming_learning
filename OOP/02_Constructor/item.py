class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


    def calculate_total_price(self):
        return self.price * self.quantity


item1 = Item("Iphone 14", 150000, 1)
item2 = Item("Asus VivoBook Laptop", 94000, 2)

print(f"Total price for {item1.name} purchase: {item1.calculate_total_price()} BDT")
print(f"Total price for {item2.name} purchase: {item2.calculate_total_price()} BDT")
