from dessert import (Candy)


def test_Candy():
    testcandy = Candy("snickers",3.5,1.60)
    assert testcandy.name == "snickers"
    assert testcandy.candy_weight == 3.5
    assert testcandy.price_per_pound == 1.60