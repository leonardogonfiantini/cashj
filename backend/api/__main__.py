from fastapi import FastAPI, HTTPException, Depends
from  database import SessionLocal
from sqlalchemy.orm import Session

import crud
from models import CategoryCreate, SupplierCreate, ProductCreate, RawProductCreate, ProductRecipeCreate, OrderCreate, OrderDetailsCreate, TransactionCreate

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/category/")
async def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db=db, category=category)


@app.get("/category/{name}")
async def read_category(name: str, db: Session = Depends(get_db)):
    db_category = crud.get_category(db=db, name=name)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category


@app.get("/categories/")
async def read_categories(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_categories(db=db, skip=skip, limit=limit)


@app.post("/supplier/")
async def create_supplier(supplier: SupplierCreate, db: Session = Depends(get_db)):
    return crud.create_supplier(db=db, supplier=supplier)

@app.get("/supplier/{name}")
async def read_supplier(name: str, db: Session = Depends(get_db)):
    db_supplier = crud.get_supplier(db=db, name=name)
    if db_supplier is None:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return db_supplier

@app.get("/suppliers/")
async def read_suppliers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_suppliers(db=db, skip=skip, limit=limit)

@app.post("/product/")
async def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db=db, product=product)

@app.get("/product/{id_prod}")
async def read_product(id_prod: int, db: Session = Depends(get_db)):
    db_product = crud.get_product(db=db, id_prod=id_prod)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@app.get("/products/")
async def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_products(db=db, skip=skip, limit=limit)

@app.post("/raw_product/")
async def create_raw_product(raw_product: RawProductCreate, db: Session = Depends(get_db)):
    return crud.create_raw_product(db=db, raw_product=raw_product)

@app.get("/raw_product/{id_raw}")
async def read_raw_product(id_raw: int, db: Session = Depends(get_db)):
    db_raw_product = crud.get_raw_product(db=db, id_raw=id_raw)
    if db_raw_product is None:
        raise HTTPException(status_code=404, detail="Raw Product not found")
    return db_raw_product

@app.get("/raw_products/")
async def read_raw_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_raw_products(db=db, skip=skip, limit=limit)

@app.post("/product_recipe/")
async def create_product_recipe(product_recipe: ProductRecipeCreate, db: Session = Depends(get_db)):
    return crud.create_product_recipe(db=db, product_recipe=product_recipe)

@app.post("/order/")
async def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    return crud.create_order(db=db, order=order)

@app.post("/order_details/")
async def create_order_details(order_details: OrderDetailsCreate, db: Session = Depends(get_db)):
    return crud.create_order_details(db=db, order_details=order_details)

@app.post("/transaction/")
async def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    return crud.create_transaction(db=db, transaction=transaction)

@app.get("/transaction/{id_transaction}")
async def read_transaction(id_transaction: int, db: Session = Depends(get_db)):
    db_transaction = crud.get_transaction(db=db, id_transaction=id_transaction)
    if db_transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return db_transaction

@app.get("/transactions/")
async def read_transactions(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_transactions(db=db, skip=skip, limit=limit)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
