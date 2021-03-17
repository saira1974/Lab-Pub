import unittest

from src.pub import Pub

from src.customer import Customer

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
    
    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.till)

    
    def test_check_age(self):
        customer = Customer("Dan", 100.00, 26)
        legal_age = self.pub.check_age(customer.age)
        self.assertEqual(True, legal_age)
    
    
        