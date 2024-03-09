from sqlalchemy import Column, Integer, String, Text, DateTime, Numeric, ForeignKey
from sqlalchemy.orm import relationship  # Import relationship function
from sqlalchemy.ext.declarative import declarative_base
from database import Base

class Category(Base):
    __tablename__ = "categories"

    name = Column(String(255), primary_key=True)
    description = Column(Text)

class Supplier(Base):
    __tablename__ = "suppliers"

    id_supplier = Column(Integer, primary_key=True)
    name = Column(String(255))
    address = Column(String(255))
    phone = Column(String(20))
    email = Column(String(255))

class Product(Base):
    __tablename__ = "products"

    id_prod = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(Text)
    price_u_table = Column(Numeric(10, 2))
    price_u_retail = Column(Numeric(10, 2))
    category_name = Column(String(255), ForeignKey('categories.name'))
    category = relationship("Category")

class RawProduct(Base):
    __tablename__ = "raw_products"

    id_raw = Column(Integer, primary_key=True)
    name = Column(String(255))
    uom = Column(String(10))
    amount = Column(Numeric(10, 4))

class ProductRecipe(Base):
    __tablename__ = "product_recipes"

    id_prod = Column(Integer, ForeignKey('products.id_prod'), primary_key=True)
    id_raw = Column(Integer, ForeignKey('raw_products.id_raw'), primary_key=True)
    amount = Column(Numeric(10, 4))

class Order(Base):
    __tablename__ = "orders"

    id_order = Column(Integer, primary_key=True)
    date = Column(DateTime)
    table_number = Column(String(20))

class OrderDetails(Base):
    __tablename__ = "order_details"

    id_order = Column(Integer, ForeignKey('orders.id_order'), primary_key=True)
    id_prod = Column(Integer, ForeignKey('products.id_prod'), primary_key=True)
    quantity = Column(Integer)
    discount = Column(Numeric(10, 2))

class Transaction(Base):
    __tablename__ = "transactions"

    id_supplier = Column(Integer, ForeignKey('suppliers.id_supplier'), primary_key=True)
    id_raw = Column(Integer, ForeignKey('raw_products.id_raw'), primary_key=True)
    date = Column(DateTime, primary_key=True)
    amount = Column(Numeric(10, 4))
    price = Column(Numeric(10, 2))
