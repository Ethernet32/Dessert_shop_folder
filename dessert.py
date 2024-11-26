from abc import ABC, abstractmethod
class DessertItem(ABC):
    def __init__(self, name):
        self.name = name
        self.tax_percent = 7.25

    def __str__(self):
        return f"{self.name}"
    @abstractmethod
    def  calculate_cost(self):
        pass
    def calculate_tax(self):
        return self.calculate_cost()*(self.tax_percent/100)

class Candy(DessertItem):
    def __init__(self, name, candy_weight, price_per_pound):
        super().__init__(name)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound

    def calculate_cost(self):
        return self.candy_weight*self.price_per_pound
    
    def __str__(self):
        return f"{self.name}, {self.candy_weight}lbs, ${self.price_per_pound}/lb, ${self.calculate_cost}, {self.calculate_tax()}"

class Cookie(DessertItem):
    def __init__(self, name, cookie_quantity, price_per_dozen):
        super().__init__(name)
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen
    
    def calculate_cost(self):
        return self.price_per_dozen*(self.cookie_quantity/12)
    
    def __str__(self):
        return f"{self.name}, {self.cookie_quantity}, ${self.price_per_dozen}/lb, ${self.calculate_cost}, {self.calculate_tax()}"

class IceCream(DessertItem):
    def __init__(self, name, scoop_count, price_per_scoop):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop
    
    def calculate_cost(self):
        return self.scoop_count*self.price_per_scoop
    
    def __str__(self):
        return f"{self.name}, {self.scoop_count}, ${self.price_per_scoop}/lb, ${self.calculate_cost}, {self.calculate_tax()}"

class Sundae(IceCream):
    def __init__(self, name, scoop_count, price_per_scoop, topping_name, topping_price):
        super().__init__(name, scoop_count, price_per_scoop)
        self.topping_name = topping_name
        self.topping_price = topping_price

    def calculate_cost(self):
        return self.scoop_count*self.price_per_scoop+ self.topping_price
    
    def __str__(self):
        return f"{ self.name}, {self.scoop_count}, ${self.price_per_scoop}/lb, {self.topping_name}, {self.topping_price}, ${self.calculate_cost}, {self.calculate_tax()}"