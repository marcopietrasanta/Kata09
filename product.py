
class Product:
    def __init__(self, id: str, price: int, discountQnt: int, discountPrice: int) -> None:
        self.id = id
        self.price = price
        self.discountQnt = discountQnt
        self.discountPrice = discountPrice