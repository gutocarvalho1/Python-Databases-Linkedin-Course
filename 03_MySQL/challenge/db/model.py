from decimal import Decimal
from sqlalchemy import String, Numeric, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from db.database import engine


class Base(DeclarativeBase):
    pass

class Customer(Base):
    __tablename__ = "customer"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))

    orders: Mapped[list["Order"]] = relationship(back_populates="customer")

    def __repr__(self):
        return f"<Customer(id={self.id}, name='{self.name}')>"
    
class Product(Base):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    category: Mapped[str] = mapped_column(String(30))
    unit_price: Mapped[Decimal] = mapped_column(Numeric(10, 2))

    orders: Mapped[list["Order"]] = relationship(back_populates="product")

    def __repr__(self):
        return f"<Product(id={self.id}, name='{self.name}', category='{self.category}', unit_price={self.unit_price})>"
    
class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(String(30))
    customer_id: Mapped[int] = mapped_column(ForeignKey("customer.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"))

    quantity: Mapped[int]
    discount: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    product_unit_price: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    order_total: Mapped[Decimal] = mapped_column(Numeric(10, 2))

    customer: Mapped[Customer] = relationship(back_populates="orders")
    product: Mapped[Product] = relationship(back_populates="orders")
    
    def __repr__(self):
        return f"<Order(id={self.id}, type='{self.type}', order_total={self.order_total})>"

Base.metadata.create_all(engine)