"""Checkout coordinates an order and a chosen payment method."""

from orders import Order
from payments import PaymentMethod, PaymentReceipt


class Checkout:
    def __init__(self, order: Order, payment_method: PaymentMethod) -> None:
        self.order = order
        self.payment_method = payment_method

    def complete(self) -> PaymentReceipt:
        if not self.order.items:
            raise ValueError("Cannot checkout an empty order.")
        amount = self.order.total()
        return self.payment_method.pay(amount)
