from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    class Config:
        orm_mode = True

class SupplierBase(BaseModel):
    name: str
    address: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None

class SupplierCreate(SupplierBase):
    pass

class Supplier(SupplierBase):
    id_supplier: int

    class Config:
        orm_mode = True

class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price_u_table: float
    price_u_retail: float
    category_name: Optional[str] = None

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id_prod: int
    category: Optional[Category]

    class Config:
        orm_mode = True

class RawProductBase(BaseModel):
    name: str
    uom: str
    amount: float

class RawProductCreate(RawProductBase):
    pass

class RawProduct(RawProductBase):
    id_raw: int

    class Config:
        orm_mode = True

class ProductRecipeBase(BaseModel):
    id_prod: int
    id_raw: int
    amount: float

class ProductRecipeCreate(ProductRecipeBase):
    pass

class ProductRecipe(ProductRecipeBase):
    class Config:
        orm_mode = True

class OrderBase(BaseModel):
    date: datetime
    table_number: str

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id_order: int

    class Config:
        orm_mode = True

class OrderDetailsBase(BaseModel):
    id_order: int
    id_prod: int
    quantity: int
    discount: Optional[float] = None

class OrderDetailsCreate(OrderDetailsBase):
    pass

class OrderDetails(OrderDetailsBase):
    class Config:
        orm_mode = True

class TransactionBase(BaseModel):
    id_supplier: int
    id_raw: int
    date: datetime
    amount: float
    price: Optional[float] = None

class TransactionCreate(TransactionBase):
    pass

class Transaction(TransactionBase):
    class Config:
        orm_mode = True
