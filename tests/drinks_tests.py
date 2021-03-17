import unittest

from src.drinks import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("vodka", 1.99, 4)

    
    def test_drink_has_name(self):
        self.assertEqual("vodka", self.drink.name)
    
    def test_drink_has_price(self):
        self.assertEqual(1.99, self.drink.price)