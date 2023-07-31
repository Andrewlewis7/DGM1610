from dessert import DessertItem, Candy, Cookie, IceCream, Sundae, Order
import pytest

def test_order_init():
    o = Order()

    o.set_pay_type("CASH")
    assert o.pay_type == "CASH"

    o.set_pay_type("CARD")
    assert o.pay_type == "CARD"

    o.set_pay_type("PHONE")
    assert o.pay_type == "PHONE"

def test_order_invalid_pay_type():
    o = Order()

    with pytest.raises(ValueError) as error:
        o.set_pay_type("INVALID_TYPE")

    assert str(error.value) == "Invalid payment type!"

def test_order_invalid_get_type():
    o = Order()
    
    with pytest.raises(ValueError) as error:
        o.pay_type = "red"
        o.get_pay_type()

    assert str(error.value) == "Invalid payment type!"
        



    
