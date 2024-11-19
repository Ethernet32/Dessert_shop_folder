from dessert import DessertItem, Candy


def test_Candy():
    test = Candy("snickers",3.5,1.60)
    assert test.calculate_cost() == test.candy_weight*test.price_per_pound
    assert test.calculate_tax() == test.calculate_cost()*(test.tax_percent/100)

