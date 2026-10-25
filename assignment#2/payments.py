"""Interchangeable simulated payment methods."""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class PaymentReceipt:
    method: str
    amount_due: Decimal
    amount_paid: Decimal
    change: Decimal
    message: str


class PaymentMethod(ABC):
    """Interface used by checkout, regardless of payment type."""

    @abstractmethod
    def pay(self, amount: Decimal) -> PaymentReceipt:
        """Simulate a payment and return the outcome."""


class CardPayment(PaymentMethod):
    """Simulated card payment; stores only a masked identifier."""

    def __init__(self, last_four: str) -> None:
        if len(last_four) != 4 or not last_four.isdigit():
            raise ValueError("Use exactly the last four card digits.")
        self.last_four = last_four

    def pay(self, amount: Decimal) -> PaymentReceipt:
        return PaymentReceipt(
            method=f"Card ending ****{self.last_four}",
            amount_due=amount,
            amount_paid=amount,
            change=Decimal("0.00"),
            message="Card payment approved (simulation).",
        )


class CashPayment(PaymentMethod):
    """Cash payment; requires enough cash and returns any change."""

    def __init__(self, cash_given: Decimal) -> None:
        cash_given = Decimal(str(cash_given))
        if not cash_given.is_finite() or cash_given < 0:
            raise ValueError("Cash given must be a non-negative number.")
        self.cash_given = cash_given.quantize(Decimal("0.01"))

    def pay(self, amount: Decimal) -> PaymentReceipt:
        if self.cash_given < amount:
            raise ValueError("Not enough cash to complete payment.")
        return PaymentReceipt(
            method="Cash",
            amount_due=amount,
            amount_paid=self.cash_given,
            change=self.cash_given - amount,
            message="Cash payment accepted (simulation).",
        )
