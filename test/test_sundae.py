from dessert import (DessertItem,Sundae)


def test_Sundae():
    test = Sundae("banana split", 3, 4.53,"Green bits", 0.1)
    assert test.calculate_cost() == test.scoop_count*test.price_per_scoop+ test.topping_price
    assert test.calculate_tax() == test.calculate_cost()*(test.tax_percent/100)