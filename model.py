from itertools import product
from typing import Optional, List

from sqlmodel import Field, Relationship, Session, SQLModel, create_engine

from pydantic import BaseModel

#order_item model
class OrderItem(SQLModel, table=True):
    order_id: int = Field(default=None, foreign_key="order.id", primary_key=True)
    product_id: int = Field(default=None, foreign_key="product.id", primary_key=True)
    customer_id: int = Field(default=None, foreign_key="customer.id", primary_key=False)
    order: "Order" = Relationship(back_populates="order_items")
    #product: "Product" = Relationship(back_populates="order_items")
    customer: "Customer" = Relationship()
    quantity: int

#product model
class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, unique=True,)
    name: str
    price: float
    order_items: List["OrderItem"] = Relationship()

#order model with cascading on to remove all order_items of particular order when order is deleted
class Order(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, unique=True,)
    amount: float
    customer_id: Optional[int] = Field(default=None, foreign_key="customer.id", primary_key=False)
    customer: "Customer" = Relationship()
    order_items: List["OrderItem"] = Relationship(back_populates="order", sa_relationship_kwargs={"cascade": "delete,all"})

#customer model
class Customer(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, unique=True)
    name: str
    phone: str
    address: str
    order_items: List["Order"] = Relationship(back_populates="customer", sa_relationship_kwargs={"cascade": "delete,all"})

#list model for passing list of order items
class ProductList(BaseModel):
    data: List[OrderItem]


#db related stuffs
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

if __name__ == "__main__":
    create_db_and_tables()