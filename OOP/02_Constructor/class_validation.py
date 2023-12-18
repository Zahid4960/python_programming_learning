class Item:
    def __init__(self, name: str, price: float, quantity: float):
        assert price >= 0, f"Price can not less than zero"
        assert quantity >= 0, f"Quantity can not less than zero"

        self.name = name
        self.price = price
        self.quantity = quantity


    def calculate_total_price(self):
        return self.price * self.quantity


item1 = Item("Iphone 14", -150000, 1) # AssertionError: Price can not less than zero
item2 = Item("Asus VivoBook", 94000, 2)
