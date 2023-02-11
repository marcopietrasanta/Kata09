from checkout import Checkout 

DS_FILENAME = "datasource.csv"

def main():    
    print(price("ABCDAAA"))


def price(goods):
    co = Checkout(DS_FILENAME)
    for item in goods:
        co.scan(item)
    return co.getTotal()


main()