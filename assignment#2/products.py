"""Product types and their pricing rules."""

from abc import ABC, abstractmethod
from decimal import Decimal


class Product(ABC):
    """Common product information and the pricing operation."""

    def __init__(self, name: str, price: Decimal) -> None:
        if not name.strip():
            raise ValueError("Product name cannot be empty.")
        price = Decimal(str(price))
        if not price.is_finite() or price < 0:
            raise ValueError("Product price must be a non-negative number.")
        self.name = name
        self.price = price.quantize(Decimal("0.01"))

    @abstractmethod
    def unit_cost(self) -> Decimal:
        """Return the final cost for one unit of this product."""


class PhysicalProduct(Product):
    """A shipped product; the price includes per-unit shipping."""

    def __init__(self, name: str, price: Decimal, shipping_cost: Decimal) -> None:
        super().__init__(name, price)
        shipping_cost = Decimal(str(shipping_cost))
        if not shipping_cost.is_finite() or shipping_cost < 0:
            raise ValueError("Shipping cost must be a non-negative number.")
        self.shipping_cost = shipping_cost.quantize(Decimal("0.01"))

    def unit_cost(self) -> Decimal:
        return self.price + self.shipping_cost


class DigitalProduct(Product):
    """A downloadable product with no shipping charge."""

    def unit_cost(self) -> Decimal:
        return self.price
