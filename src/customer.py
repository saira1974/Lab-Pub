class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = 0
    
    def buy_drink(self, pub, drink):
        for d in pub.drinks:
            if drink.name == d and pub.check_age(self.age) and self.drunkenness < 15:
                self.wallet -= drink.price
                pub.till += drink.price
                self.drunkenness += drink.alcohol_level
            else:
                return "Sorry no"
        

    
