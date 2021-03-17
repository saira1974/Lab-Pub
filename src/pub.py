class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = ["vodka", "baileys", "guiness"]
    
    def check_age(self, age):
        if age >= 18:
            return True
        else:
            return False
    

    def check_drunkenness(self, drunkenness):
        if drunkenness < 15:
            return True
        else:
            return False