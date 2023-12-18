class Item:
    @staticmethod
    def calculate_total_price(x, y):
        return x * y


item1 = Item()
item1.name = "Phone 15"
item1.quantity = 1
item1.price = 150000
total_for_item1 = item1.calculate_total_price(item1.price, item1.quantity)

item2 = Item()
item2.name = "Asus VivoBook Laptop"
item2.price = 94000
item2.quantity = 2
total_for_item2 = item2.calculate_total_price(item2.price, item2.quantity)

print(f"Total price for {item1.name} purchase: {total_for_item1} BDT")
print(f"Total price for {item2.name} purchase: {total_for_item2} BDT")
