from dessert import (Cookie)


def test_Cookie():
    testcookie = Cookie("snickerdoodle",6,1.20)
    assert testcookie.name == "snickerdoodle"
    assert testcookie.cookie_quantity == 6
    assert testcookie.price_per_dozen == 1.20