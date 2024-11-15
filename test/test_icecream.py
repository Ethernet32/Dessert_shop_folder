from dessert import (IceCream)


def test_IceCream():
    testicecream = IceCream("green", 3, 4.53)
    assert testicecream.name == "green"
    assert testicecream.scoop_count == 3
    assert testicecream.price_per_scoop == 4.53