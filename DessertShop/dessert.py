from abc import abstractmethod
from packaging import Packaging
from payment import Payable

class DessertItem(Packaging):
    def __init__(self, name = "", tax_percent = 7.25, packaging = None) -> None:
        self.name = name
        self.tax_percent = tax_percent
        self.packaging = packaging

    @abstractmethod
    def calculate_cost(self):
        pass

    def calculate_tax(self):
        return round(self.calculate_cost() * (self.tax_percent / 100), 2)




class Candy(DessertItem):
    def __init__(self, name = "", candy_weight = 0.0, price_per_pound = 0.0, packaging = "Bag" ):
        super().__init__(name, packaging=packaging)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound

    def calculate_cost(self):
        return round(self.candy_weight * self.price_per_pound, 2)

    def __str__(self):
        return f'{self.name} ({self.packaging})', f'{self.candy_weight}lbs', f'${self.price_per_pound}/lb', f'${self.calculate_cost()}', f'${self.calculate_tax()}'
    

class Cookie(DessertItem):
    def __init__(self, name = "", cookie_quantity = 0.0, price_per_dozen = 0.0, packaging = "Box"):
        super().__init__(name, packaging=packaging)
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen

    def calculate_cost(self):
        return round(self.cookie_quantity / 12 * self.price_per_dozen, 2)
    
    def __str__(self):
        return f'{self.name} ({self.packaging})', f'{self.cookie_quantity} cookies', f'${self.price_per_dozen}/dozen', f'${self.calculate_cost()}', f'${self.calculate_tax()}'
    
class IceCream(DessertItem):
    def __init__(self, name = "", scoop_count = 0.0, price_per_scoop = 0.0, packaging = "Bowl"):
        super().__init__(name, packaging=packaging)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop

    def calculate_cost(self):
        return round(self.scoop_count * self.price_per_scoop, 2)
    
    def __str__(self):
        return f'{self.name} ({self.packaging})', f'{self.scoop_count} scoops', f'${self.price_per_scoop}/scoop', f'${self.calculate_cost()}', f'${self.calculate_tax()}'
    
class Sundae(IceCream):
    def __init__(self, name = "", scoop_count = 0.0, price_per_scoop = 0.0, \
                topping_name = "", topping_price = 0.0, packaging = "Boat"):
        super().__init__(name, scoop_count, price_per_scoop, packaging=packaging)
        self.topping_name = topping_name
        self.topping_price = topping_price
    
    def calculate_cost(self):
        return round(self.scoop_count * self.price_per_scoop + self.topping_price, 2)
    
    def __str__(self):
        base_info = f'{self.name} ({self.packaging})', f'{self.scoop_count} scoops', f'${self.price_per_scoop}/scoop', \
                    f'${self.calculate_cost()}', f'${self.calculate_tax()}'
        toppings_info = f'\n{self.topping_name}', "1", f'${self.topping_price}'
        return base_info, toppings_info

class Order(Payable):
    def __init__(self, PayType: list[str] = ["CASH", "CARD", "PHONE"]):
        self.order: list[str] = []
        self.PayType = PayType
        self.pay_type = PayType[0]

    @property
    def get_pay_type(self):
        if self.pay_type not in self.PayType:
            raise ValueError("Invalid payment type!")
        return self.pay_type
    
    def set_pay_type(self, payment_method):
        if payment_method not in self.PayType:
            raise ValueError("Invalid payment type!")
        self.pay_type = payment_method

    def add(self, item):
        if isinstance(item, DessertItem):
            self.order.append(item)
        else:
            raise ValueError("Only DessertItem objects can be added to the order.")

    def __len__(self):
        return len(self.order)

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < len(self.order):
            item = self.order[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration
    
    def order_cost(self):
        total_cost = 0
        for item in self.order:
            total_cost += item.calculate_cost()
        return round(total_cost, 2)

    def order_tax(self):
        total_tax = 0
        for item in self.order:
            total_tax += item.calculate_tax()
        return round(total_tax, 2)
        
    def __str__(self):
        for item in self.order:
            print(item.__str__())
        print(f'Paid with {self.pay_type}')

        

# s = Sundae('Vanilla', 3, 0.69, 'Hot Fudge', 1.29)

# print(s.__str__())
