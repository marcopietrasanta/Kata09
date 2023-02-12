from product import Product
import re

SPECIAL_PRICE_FORMAT = r'(\d+) for (\d+)'

class RuleParser:

    @staticmethod
    def parse(filename) -> dict[str, Product]:
        rules = {}
        try:
            with open(filename) as source_file:
                for line in source_file.readlines():
                    itemId, price, special = line.strip().split(";")
                    discountQnt = discountPrice = None
                    if special:
                        numbers_found = re.search(SPECIAL_PRICE_FORMAT, special)
                        discountQnt = int(numbers_found.group(1))
                        discountPrice = int(numbers_found.group(2))

                    rules[itemId] = Product(itemId, int(price), discountQnt, discountPrice)
        except IOError:
            exit(f"File {filename} not found")
        return rules