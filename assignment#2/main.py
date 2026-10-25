"""Run two complete shopping/checkout demonstrations."""

from decimal import Decimal

from checkout import Checkout
from orders import Order
from payments import CardPayment, CashPayment, PaymentMethod, PaymentReceipt
from products import DigitalProduct, PhysicalProduct


def make_sample_order() -> Order:
    """Create a fresh order so each demo is a separate transaction."""
    order = Order()
    order.add_product(
        PhysicalProduct("Keyboard", Decimal("50.00"), Decimal("5.00")),
        quantity=1,
    )
    order.add_product(DigitalProduct("E-book", Decimal("20.00")), quantity=2)
    return order


def demonstrate_checkout(label: str, payment_method: PaymentMethod) -> None:
    order = make_sample_order()
    print(f"\n=== {label} CHECKOUT ===")
    print("Items (unit cost includes shipping, when applicable):")
    for item in order.items:
        print(
            f"  {item.product.name} x{item.quantity} "
            f"@ ${item.product.unit_cost():.2f} = ${item.line_total():.2f}"
        )
    receipt: PaymentReceipt = Checkout(order, payment_method).complete()
    print(f"Order total: ${order.total():.2f}")
    print(f"Payment method: {receipt.method}")
    print(f"Amount paid: ${receipt.amount_paid:.2f}")
    print(f"Change: ${receipt.change:.2f}")
    print(receipt.message)


def main() -> None:
    print("ONLINE SHOPPING AND PAYMENT PROCESSING SYSTEM")
    demonstrate_checkout("CARD", CardPayment("1234"))
    demonstrate_checkout("CASH", CashPayment(Decimal("100.00")))


if __name__ == "__main__":
    main()
