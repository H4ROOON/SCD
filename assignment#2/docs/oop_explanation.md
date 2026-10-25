# Assignment #2 — OOP Design Explanation

## Inheritance

The system has two abstract base classes. `Product` stores the information that all products share (`name` and `price`) and declares the `unit_cost()` operation. `PhysicalProduct` and `DigitalProduct` inherit from it because both are kinds of products. The physical product adds a shipping cost, while the digital product needs no shipping. Likewise, `PaymentMethod` declares the `pay(amount)` operation. Its subclasses, `CardPayment` and `CashPayment`, are different ways to make a payment. These inheritance relationships remove duplicated common interfaces and give the system meaningful "is-a" relationships.

## Polymorphism

Polymorphism allows the same operation to work on different object types. The order calls `item.product.unit_cost()` without checking which type of product it received. A `PhysicalProduct` includes shipping in the returned unit cost; a `DigitalProduct` returns the download price. This also means another product type could be added without rewriting `Order.total()`. During checkout, `Checkout.complete()` calls `self.payment_method.pay(amount)` without checking whether the method is card or cash. Card payment produces a simulated approval with no change, while cash payment checks the amount tendered and calculates change. Both return the same `PaymentReceipt` format.

## Composition

An `Order` creates and owns a collection of `OrderItem` objects. Each `OrderItem` stores a reference to a `Product` and a quantity. This is composition: the line items belong to a particular order, whereas the product itself may exist independently. Keeping the quantity inside an order item makes the relationship more practical than storing a bare list of products. `Checkout` holds references to an existing `Order` and a selected `PaymentMethod`; these are associations ("uses" relationships), not strict ownership, because those objects can exist without checkout.

## Responsibility and design decisions

The code is separated into `products.py` for pricing rules, `orders.py` for shopping totals, `payments.py` for payment behaviours, `checkout.py` for coordinating payment, and `main.py` for the demonstration. Money uses Python's `Decimal` type to avoid common floating-point rounding issues. The example includes one keyboard priced at $50 with $5 shipping and two e-books costing $20 each, making the order total $95. Two independent sample orders demonstrate a simulated $95 card payment and a $100 cash payment that returns $5 change. The application is educational and does **not** contact a bank or process real card information.
