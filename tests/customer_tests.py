import unittest

from src.pub import Pub

from src.customer import Customer

from src.drinks import Drink



class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Dan", 100.00, 26)
    
    def test_customer_has_name(self):
        self.assertEqual("Dan", self.customer.name)
    
    def test_customer_has_wallet(self):
        self.assertEqual(100.00, self.customer.wallet)
    
    def test_buy_drink(self):
        pub = Pub("The Prancing Pony", 100.00)
        drink = Drink("vodka", 1.99, 4)
        self.customer.buy_drink(pub, drink)
        self.assertEqual(98.01, self.customer.wallet)
        self.assertEqual(101.99, pub.till)

    
    def test_buy_drink_none(self):
        pub = Pub("The Prancing Pony", 100.00)
        drink = Drink("tennants", 5.00, 2)
        response = self.customer.buy_drink(pub, drink)
        self.assertEqual("Sorry no", response)
    
    def test_customer_has_age(self):
        self.assertEqual(26, self.customer.age)
    
    def test_drunkenness(self):
        pub = Pub("The Prancing Pony", 100.00)
        drink = Drink("vodka", 1.99, 4)
        self.customer.buy_drink(pub, drink)
        self.assertEqual(drink.alcohol_level,self.customer.drunkenness)
    
    def test_age_limit(self):
        pub = Pub("The Prancing Pony", 100.00)
        drink = Drink("vodka", 1.99, 4)
        self.customer.age = 17
        response = self.customer.buy_drink(pub, drink)
        self.assertEqual("Sorry no", response)
    
  