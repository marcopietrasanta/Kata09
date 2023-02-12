import unittest
from checkout import Checkout
from rule_parser import RuleParser

DS_FILENAME = "datasource.csv"
RULES = RuleParser.parse(DS_FILENAME)

class CheckoutTest(unittest.TestCase):
    def price(self, goods):
        co = Checkout(RULES)
        for item in goods:
            co.scan(item)
        return co.total()

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
        co = Checkout(RULES)
        self.assertEqual(  0, co.total())
        co.scan("A");  self.assertEqual( 50, co.total())
        co.scan("B");  self.assertEqual( 80, co.total())
        co.scan("A");  self.assertEqual(130, co.total())
        co.scan("A");  self.assertEqual(160, co.total())
        co.scan("B");  self.assertEqual(175, co.total())


if __name__ == '__main__':
    unittest.main()