from pydantic import BaseModel
from typing import Optional

from pydantic import BaseModel
from typing import List, Optional

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
    category: Optional[Category] = None

    class Config:
        orm_mode = True

class RawProductBase(BaseModel):
    name: str
    uom: Optional[str] = None
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
    pass

class OrderBase(BaseModel):
    date: str
    billNo: int
    table: str
    discount: Optional[float] = None
    price: float
    order_details: dict

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    pass

class TransactionBase(BaseModel):
    id_supplier: int
    id_raw: int
    date: str
    amount: float
    price: Optional[float] = None

class TransactionCreate(TransactionBase):
    pass

class Transaction(TransactionBase):
    pass
