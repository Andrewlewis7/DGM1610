from dessert import DessertItem, Candy, Cookie, IceCream, Sundae

def test_sundae_init():
    s = Sundae()
    assert s.name == ""
    assert s.scoop_count == 0.0
    assert s.price_per_scoop == 0.0
    assert s.topping_name == ""
    assert s.topping_price == 0.0
    assert isinstance(s, DessertItem)
    assert issubclass(Sundae, DessertItem)

    s = Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29)
    assert s.calculate_tax() == 0.24


