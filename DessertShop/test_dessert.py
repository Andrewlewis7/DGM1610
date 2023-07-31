from dessert import DessertItem, Candy, Cookie, IceCream, Sundae





def test_dessertitem_init():
    di = Candy('Candy Corn', 1.5, 0.25)
    assert isinstance(di.name, str)
    assert isinstance(di.tax_percent, float)
    assert di.tax_percent == 7.25
    assert di.packaging == "Bag"


def test_calculate_cost():
    c = Candy("Candy Corn", 1.5, .25)
    co = Cookie("Chocolate Chip", 6, 3.99)
    i = IceCream("Pistachio", 2, .79)
    s = Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29)
    assert i.calculate_cost() == 1.58
    assert c.calculate_cost() == 0.38
    assert co.calculate_cost() == 2.0
    assert s.calculate_cost() == 3.36


    