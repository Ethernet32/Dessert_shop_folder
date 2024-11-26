from dessert import DessertItem,Cookie


def test_Cookie():
    test = Cookie("snickerdoodle",6,1.20)
    assert test.calculate_cost() == test.price_per_dozen*(test.cookie_quantity/12)
    assert test.calculate_tax() == test.calculate_cost()*(test.tax_percent/100)
    assert test.packaging == "Box"