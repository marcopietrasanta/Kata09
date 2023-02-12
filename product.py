
class Product:
    def __init__(self, id: str, price: int, discountQnt: int, discountPrice: int) -> None:
        self.id = id
        self.price = price
        self.discountQnt = discountQnt
        self.discountPrice = discountPrice
        self.noDiscount = discountQnt is None or discountPrice is None

    
    def getPrice(self, n: int) -> int:
        if self.noDiscount:
            return n * self.price
        return (n // self.discountQnt) * self.discountPrice + (n % self.discountQnt) * self.price