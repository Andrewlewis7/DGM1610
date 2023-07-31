from dessert import DessertItem, Candy, Cookie, IceCream, Sundae

def test_cookie_init():
    cookie = Cookie()
    assert cookie.name == ""
    assert cookie.cookie_quantity == 0.0
    assert cookie.price_per_dozen == 0.0
    assert cookie.packaging == "Box"
    assert isinstance(cookie, DessertItem)
    assert issubclass(Cookie, DessertItem)

    c = Cookie("Chocolate Chip", 6, 3.99)
    assert c.calculate_tax() == 0.14

    