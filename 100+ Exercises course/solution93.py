class Laptop:

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        if not isinstance(price,(int,float)):
            raise TypeError
        else:
            self.price = price