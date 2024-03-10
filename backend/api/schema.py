from sqlalchemy import Column, ForeignKey, Integer, Numeric, String, Text, DateTime, UniqueConstraint
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from database import Base

class Category(Base):
    __tablename__ = "Category"
    name = Column(String(255), primary_key=True)
    description = Column(Text)

class Supplier(Base):
    __tablename__ = "Supplier"
    id_supplier = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    address = Column(String(255))
    phone = Column(String(20))
    email = Column(String(255))

class Product(Base):
    __tablename__ = "Product"
    id_prod = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    price_u_table = Column(Numeric(10, 2), nullable=False)
    price_u_retail = Column(Numeric(10, 2), nullable=False)
    category_name = Column(String(255), ForeignKey('Category.name', ondelete="SET NULL"))
    category = relationship("Category")

class RawProduct(Base):
    __tablename__ = "Raw_Product"
    id_raw = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    uom = Column(String(10))
    amount = Column(Numeric(10, 4), nullable=False)

class ProductRecipe(Base):
    __tablename__ = "Product_Recipe"
    id_prod = Column(Integer, ForeignKey('Product.id_prod', ondelete="CASCADE"), primary_key=True)
    id_raw = Column(Integer, ForeignKey('Raw_Product.id_raw', ondelete="CASCADE"), primary_key=True)
    amount = Column(Numeric(10, 4), nullable=False)
    product = relationship("Product")
    raw_product = relationship("RawProduct")

class Order(Base):
    __tablename__ = "Order"

    billNo = Column(Integer, nullable=False, primary_key=True)
    
    date = Column(DateTime, nullable=False)
    table = Column(String(30), nullable=False)
    
    discount = Column(Numeric(10, 2))
    price = Column(Numeric(10, 2), nullable=False)
    
    order_details = Column(JSONB, nullable=False)
    
    __table_args__ = (
        (UniqueConstraint('date', 'table', name='unique_order')),
    )


class Transaction(Base):
    __tablename__ = "Transaction"
    id_supplier = Column(Integer, ForeignKey('Supplier.id_supplier', ondelete="CASCADE"), primary_key=True)
    id_raw = Column(Integer, ForeignKey('Raw_Product.id_raw', ondelete="CASCADE"), primary_key=True)
    date = Column(DateTime, primary_key=True)
    amount = Column(Numeric(10, 4), nullable=False)
    price = Column(Numeric(10, 2))

