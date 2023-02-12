from checkout import Checkout 
from rule_parser import RuleParser

DS_FILENAME = "datasource.csv"

def main():    
    items = 'ABCDAAAAAAAA'
    print(f"Cart with {items} costs {price(items)}")


def price(goods):
    co = Checkout(RuleParser.parse(DS_FILENAME))
    for item in goods:
        co.scan(item)
    return co.total()


main()