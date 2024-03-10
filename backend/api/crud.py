from sqlalchemy.orm import Session
from schema import Category, Supplier, Product, RawProduct, ProductRecipe, Order, Transaction
from models import CategoryCreate, SupplierCreate, ProductCreate, RawProductCreate, ProductRecipeCreate, OrderCreate, TransactionCreate


def create_category(db: Session, category: CategoryCreate):
    db_category = Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_category(db: Session, name: str):
    return db.query(Category).filter(Category.name == name).first()

def get_categories(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Category).offset(skip).limit(limit).all()

def create_supplier(db: Session, supplier: SupplierCreate):
    db_supplier = Supplier(**supplier.dict())
    db.add(db_supplier)
    db.commit()
    db.refresh(db_supplier)
    return db_supplier

def get_supplier(db: Session, name: str):
    return db.query(Supplier).filter(Supplier.name == name).first()

def get_suppliers(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Supplier).offset(skip).limit(limit).all()

def create_product(db: Session, product: ProductCreate):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_product(db: Session, id_prod: int):
    return db.query(Product).filter(Product.id_prod == id_prod).first()

def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Product).offset(skip).limit(limit).all()

def create_raw_product(db: Session, raw_product: RawProductCreate):
    db_raw_product = RawProduct(**raw_product.dict())
    db.add(db_raw_product)
    db.commit()
    db.refresh(db_raw_product)
    return db_raw_product

def get_raw_product(db: Session, id_raw: int):
    return db.query(RawProduct).filter(RawProduct.id_raw == id_raw).first()

def get_raw_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(RawProduct).offset(skip).limit(limit).all()

def create_product_recipe(db: Session, product_recipe: ProductRecipeCreate):
    db_product_recipe = ProductRecipe(**product_recipe.dict())
    db.add(db_product_recipe)
    db.commit()
    db.refresh(db_product_recipe)
    return db_product_recipe

def get_product_recipe(db: Session, id_prod: int, id_raw: int):
    return db.query(ProductRecipe).filter(ProductRecipe.id_prod == id_prod, ProductRecipe.id_raw == id_raw).first()

def get_product_recipes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(ProductRecipe).offset(skip).limit(limit).all()

def create_order(db: Session, order: OrderCreate):
    db_order = Order(**order.dict())
    print(db_order)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_order(db: Session, id_order: int):
    return db.query(Order).filter(Order.id_order == id_order).first()

def get_orders(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Order).offset(skip).limit(limit).all()

def create_transaction(db: Session, transaction: TransactionCreate):
    db_transaction = Transaction(**transaction.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

def get_transaction(db: Session, id_supplier: int, id_raw: int, date: str):
    return db.query(Transaction).filter(Transaction.id_supplier == id_supplier, Transaction.id_raw == id_raw, Transaction.date == date).first()

def get_transactions(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Transaction).offset(skip).limit(limit).all()