import unittest
from checkout import Checkout

DS_FILENAME = "datasource.csv"

class CheckoutTest(unittest.TestCase):
    def price(self, goods):
        co = Checkout(DS_FILENAME)
        for item in goods:
            co.scan(item)
        return co.getTotal()

    def test_totals(self):
        self.assertEqual(  0, self.price(""))
        self.assertEqual( 50, self.price("A"))
        self.assertEqual( 80, self.price("AB"))
        self.assertEqual(115, self.price("CDBA"))

        self.assertEqual(100, self.price("AA"))
        self.assertEqual(130, self.price("AAA"))
        self.assertEqual(180, self.price("AAAA"))
        self.assertEqual(230, self.price("AAAAA"))
        self.assertEqual(260, self.price("AAAAAA"))

        self.assertEqual(160, self.price("AAAB"))
        self.assertEqual(175, self.price("AAABB"))
        self.assertEqual(190, self.price("AAABBD"))
        self.assertEqual(190, self.price("DABABA"))

    def test_incremental(self):
        co = Checkout(DS_FILENAME)
        self.assertEqual(  0, co.getTotal())
        co.scan("A");  self.assertEqual( 50, co.getTotal())
        co.scan("B");  self.assertEqual( 80, co.getTotal())
        co.scan("A");  self.assertEqual(130, co.getTotal())
        co.scan("A");  self.assertEqual(160, co.getTotal())
        co.scan("B");  self.assertEqual(175, co.getTotal())


if __name__ == '__main__':
    unittest.main()