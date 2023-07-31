from typing import Protocol

class Payable(Protocol):
    PayType: list[str] = ["CASH", "CARD", "PHONE"]

    @property
    def get_pay_type(self):
        if self.pay_type not in self.PayType:
            raise ValueError("Invalid payment type!")
        return self.pay_type
    
    def set_pay_type(self, payment_method):
        if payment_method not in self.PayType:
            raise ValueError("Invalid payment type!")
        self.pay_type = payment_method




