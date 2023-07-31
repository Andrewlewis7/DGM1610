from dessert import DessertItem, Candy, Cookie, IceCream, Sundae

def test_candy_init():
    c = Candy()
    assert c.name == ""
    assert c.candy_weight == 0.0
    assert c.price_per_pound == 0.0
    assert isinstance(c, DessertItem)
    assert issubclass(Candy, DessertItem)

    c = Candy("Candy Corn", 1.5, .25)
    assert c.calculate_tax() == 0.03