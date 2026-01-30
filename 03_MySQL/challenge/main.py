import os
from decimal import Decimal
from sqlalchemy.orm import Session

from db import sales
from db.database import engine

MENU = """
    Select a option:
    1 - Add customer
    2 - Add product
    3 - Add order
    4 - Exit
"""

def clear_terminal():
    _ = os.system('cls')

def crud_op(session: Session, op: int):
    match op:
        case "1":
            clear_terminal()
            customer_name = input("Enter the customer name: ")
            new_customer = sales.add_customer(session, customer_name)
            session.flush()
            print(f"Customer {customer_name} successfully added (id={new_customer.id}).")
        case "2":
            clear_terminal()
            product_name = input("Enter the product name: ")
            product_category = input("Enter the product category: ")
            product_unit_price = input("Enter the product unit price: ")
            new_product = sales.add_product(session, product_name, product_category, product_unit_price)
            session.flush()
            print(f"Product {product_name} successfully added (id={new_product.id}).")
        case "3":
            clear_terminal()
            order_type = input("Enter the order type: ")
            customer_id = input("Enter the customer id: ")
            product_id = input("Enter the product id: ")
            order_quantity = int(input("Enter the order quantity: "))
            order_discount = Decimal(input("Enter the discount amount: "))
            new_order = sales.add_order(
                session=session,
                type=order_type,
                customer_id=customer_id,
                product_id=product_id,
                quantity=order_quantity,
                discount=order_discount,
            )
            session.flush()
            print(f"Order {order_type} successfully added (id={new_order.id}).")

def main():
    with Session(engine) as session:
        while True:
            print(MENU)
            option = input()
            if option in ("1", "2", "3"):
                try:
                    crud_op(session, option)
                    session.commit()
                except Exception as e:
                    session.rollback()
                    print(f"Error ocurred, terminating session... ({e})")
                    return
            elif option == "4":
                return
            else:
                print("Please, select a valid option!")

if __name__ == "__main__":
    main()