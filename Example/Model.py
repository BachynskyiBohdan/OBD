from Example import Observable

class Model(object):
    TAX = 0.2
    def __init__(self):
        self.price = Observable(0)
    def calcPrice(self, price):
        self.price.set(price * (1 + self.TAX))