from dessert import (DessertItem,IceCream)


def test_IceCream():
    test = IceCream("green", 3, 4.53)
    assert test.calculate_cost() == test.scoop_count*test.price_per_scoop
    assert test.calculate_tax() == test.calculate_cost()*(test.tax_percent/100)