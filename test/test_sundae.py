from dessert import (Sundae)


def test_Sundae():
    testsundae = Sundae("banana split", 3, 4.53,"Green bits", 0.1)
    assert testsundae.name == "banana split"
    assert testsundae.scoop_count == 3
    assert testsundae.price_per_scoop == 4.53
    assert testsundae.topping_name == "Green bits"
    assert testsundae.topping_price == 0.1