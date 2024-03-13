from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Column, JSON, ForeignKeyConstraint
from typing import Optional, List

class Category(SQLModel, table=True):
    name: str = Field(default=None, primary_key=True)
    description: str
    
    products: List["Product"] = Relationship(back_populates="category")

class Supplier(SQLModel, table=True):
    id_supplier: int = Field(default=None, primary_key=True)
    name: str
    address: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None

class Product(SQLModel, table=True):
    id_prod: int = Field(default=None, primary_key=True)
    name: str
    description: str
    price_u_table: float
    price_u_retail: float
    category_name: str = Field(default=None, foreign_key="category.name")
    
    category: Optional[Category] = Relationship(back_populates="products")

    product_recipes: List["ProductRecipe"] = Relationship(back_populates="product")

class RawProduct(SQLModel, table=True):
    id_raw: int = Field(default=None, primary_key=True)
    name: str
    uom: str
    amount: float
    
    product_recipes: List["ProductRecipe"] = Relationship(back_populates="rawproduct")

class ProductRecipe(SQLModel, table=True):
    id_prod: int = Field(default=None, foreign_key="product.id_prod", primary_key=True)
    id_raw: int = Field(default=None, foreign_key="rawproduct.id_raw", primary_key=True)
    amount: float
    
    product: Optional[Product] = Relationship(back_populates="product_recipes")
    rawproduct: Optional[RawProduct] = Relationship(back_populates="product_recipes")
    
class Order(SQLModel, table=True):
    billNo: int = Field(default=None, primary_key=True)
    date: str
    table: str
    discount: Optional[float] = None
    price: float
    order_details: dict = Field(default={}, sa_column=Column(JSON))

    class Config:
        arbitrary_types_allowed = True

class Transaction(SQLModel, table=True):
    id_supplier: int = Field(default=None, primary_key=True)
    id_raw: int = Field(default=None, primary_key=True)
    date: str = Field(default=None, primary_key=True)
    amount: float
    price: Optional[float] = None
    