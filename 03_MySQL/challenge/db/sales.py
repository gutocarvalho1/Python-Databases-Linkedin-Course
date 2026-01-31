from decimal import Decimal
from sqlalchemy import select, func
from sqlalchemy.orm import Session

from db.model import Customer, Product, Order


def add_customer(session: Session, name: str) -> Customer:
    new_customer = Customer(name=name)
    session.add(new_customer)
    return new_customer

def add_product(
    session: Session,
    name: str,
    category: str,
    unit_price: Decimal = Decimal("0.00"),
) -> Product:
    new_product = Product(name=name, category=category, unit_price = unit_price)
    session.add(new_product)
    return new_product

def add_order(
    session: Session,
    type: str,
    customer_id: int,
    product_id: int,
    quantity: int,
    discount: Decimal,
) -> Order:
    customer = session.get(Customer, customer_id)
    product = session.get(Product, product_id)

    if customer is None:
        print(f"No customer found with id {customer_id}")
        return
    if product is None:
        print(f"No producto found with id {product_id}")
        return

    order_subtotal = quantity * product.unit_price
    order_total = order_subtotal - discount

    new_order = Order(
        type=type,
        customer_id=customer_id,
        product_id=product_id,
        quantity=quantity,
        discount=discount,
        product_unit_price=product.unit_price,
        order_total=order_total
    )

    session.add(new_order)
    return new_order

def get_most_expensive_order(session: Session) -> Order:
    smt = select(Order).order_by(Order.order_total.desc())
    return session.scalars(smt).first()

def get_product(session: Session, product_id: int) -> Product:
    return session.get(Product, product_id)

def get_customer(session: Session, customer_id: int) -> Customer:
    return session.get(Customer, customer_id)