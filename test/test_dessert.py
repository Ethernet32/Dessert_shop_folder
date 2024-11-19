from dessert import (DessertItem, Candy)


def test_dessertItem():
    test_dessert = Candy("snickers",3.5,1.60)
    assert test_dessert.tax_percent == 7.25