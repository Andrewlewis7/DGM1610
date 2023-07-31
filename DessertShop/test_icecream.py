from dessert import DessertItem, Candy, Cookie, IceCream, Sundae

def test_icecream_init():
    i = IceCream()
    assert i.name == ""
    assert i.scoop_count == 0.0
    assert i.price_per_scoop == 0.0
    assert isinstance(i, DessertItem)
    assert issubclass(IceCream, DessertItem)

    i = IceCream("Pistachio", 2, .79)
    assert i.calculate_tax() == .11