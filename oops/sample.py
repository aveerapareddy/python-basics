import csv


class Item:
    pay_rate = 0.8  # The pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run Validations to the received arguments
        assert price >= 0, f"price {price} is not greater than or equal zero!"
        assert quantity >= 0, f"price {quantity} is not greater than or equalzero!"
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to Execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def appl_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}','{self.price}','{self.quantity}')"

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=float(item.get('quantity')),
            )


item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

item2.has_numpad = False

print(Item.__dict__)
print(item1.__dict__)
print(item1.appl_discount())
print(item1.price)
item2.pay_rate = 0.7
print(item2.appl_discount())
print(item2.price)

print(Item.all)

for instance in Item.all:
    print(instance.name)

Item.instantiate_from_csv()
