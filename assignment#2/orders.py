"""Shopping orders, made up of their own line items."""

from dataclasses import dataclass
from decimal import Decimal
from products import Product


@dataclass(frozen=True)
class OrderItem:
    """One product and the number of units ordered."""

    product: Product
    quantity: int

    def line_total(self) -> Decimal:
        return self.product.unit_cost() * self.quantity


class Order:
    """Owns its order items and calculates the order total."""

    def __init__(self) -> None:
        self._items: list[OrderItem] = []

    @property
    def items(self) -> tuple[OrderItem, ...]:
        """Expose a read-only snapshot of order lines."""
        return tuple(self._items)

    def add_product(self, product: Product, quantity: int = 1) -> None:
        if not isinstance(product, Product):
            raise TypeError("Only Product objects can be added to an order.")
        if type(quantity) is not int or quantity <= 0:
            raise ValueError("Quantity must be a positive whole number.")
        self._items.append(OrderItem(product, quantity))

    def total(self) -> Decimal:
        return sum((item.line_total() for item in self._items), Decimal("0.00"))
