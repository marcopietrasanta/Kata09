from product import Product
import re

SPECIAL_PRICE_FORMAT = r'(\d+) for (\d+)'


class Checkout:
    def __init__(self, filename: str) -> None:
        self.rules = self.__parseDatasource(filename)
        self.cart = {}

    def scan(self, item):
        if item not in self.rules:
            return
        if item not in self.cart:
            self.cart[item] = 0
        self.cart[item] += 1

    def getTotal(self) -> int:
        total = 0
        for item, count in self.cart.items():
            p = self.rules[item]
            total += (count // p.discountQnt) * p.discountPrice if p.discountQnt is not None else 0
            total += (count % p.discountQnt) * p.price if p.discountQnt is not None else count * p.price

        return total

    def __parseDatasource(self, filename) -> dict[str, Product]:
        rules = {}
        try:
            with open(filename) as source_file:
                for line in source_file.readlines():
                    itemId, price, special = line.strip().split(";")
                    discountQnt = discountPrice = None
                    if not special.isspace():
                        numbers_found = re.search(SPECIAL_PRICE_FORMAT, special)
                        if numbers_found:
                            discountQnt = int(numbers_found.group(1))
                            discountPrice = int(numbers_found.group(2))

                    rules[itemId] = Product(itemId, int(price), discountQnt, discountPrice)
        except IOError:
            exit(f"File {filename} not found")
        return rules
