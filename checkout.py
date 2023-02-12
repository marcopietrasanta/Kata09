from product import Product

class Checkout:
    def __init__(self, rules: dict[str, Product]) -> None:
        self.rules = rules
        self.cart = {}

    def scan(self, item):
        if item not in self.rules:
            return
        if item not in self.cart:
            self.cart[item] = 0
        self.cart[item] += 1

    def total(self) -> int:
        total = 0
        for item, count in self.cart.items():
            total += self.rules[item].getPrice(count)
        return total

