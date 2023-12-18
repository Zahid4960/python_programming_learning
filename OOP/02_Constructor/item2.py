class Item:
    discount_in_percent = 20
    all = []

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

        self.all.append(self)


    def calculate_total_price(self):
        return self.price * self.quantity


    def calculate_discount(self):
        return (self.price * self.quantity) * (self.discount_in_percent / 100)


    def __repr__(self):
        return f"Item(Name: {self.name}, Price: {self.price}, Quantity: {self.quantity})"


item1 = Item("Iphone 14", 150000, 1)
item2 = Item("Asus VivoBook Laptop", 94000, 2)
item3 = Item("Infinix hot 11s mobile", 16000, 3)

print("Total price:")
print(f"{item1.name}: {item1.calculate_total_price()} BDT")
print(f"{item2.name}: {item2.calculate_total_price()} BDT")
print(f"{item3.name}: {item3.calculate_total_price()} BDT")

print("Discount")
print(f"{item1.name}: {item1.calculate_discount()} BDT")
print(f"{item2.name}: {item2.calculate_discount()} BDT")
print(f"{item3.name}: {item3.calculate_discount()} BDT")

print(Item.all)
