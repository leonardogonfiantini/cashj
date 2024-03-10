from fastapi import FastAPI, HTTPException, Depends
from database import SessionLocal
from sqlalchemy.orm import Session

import crud
from models import CategoryCreate, SupplierCreate, ProductCreate, RawProductCreate, ProductRecipeCreate, OrderCreate, TransactionCreate
from database import Base, engine

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/category/")
async def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_category(db=db, category=category)
    except:
        raise HTTPException(status_code=400, detail="Category already exists")

@app.get("/category/{name}")
async def read_category(name: str, db: Session = Depends(get_db)):
    try:
        return crud.get_category(db, name=name)
    except:
        raise HTTPException(status_code=404, detail="Category not found")

@app.get("/categories/")
async def read_categories(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    try:
        return crud.get_categories(db, skip=skip, limit=limit)
    except:
        raise HTTPException(status_code=404, detail="Categories not found")
    
@app.post("/supplier/")
async def create_supplier(supplier: SupplierCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_supplier(db=db, supplier=supplier)
    except:
        raise HTTPException(status_code=400, detail="Supplier already exists")
    
@app.get("/supplier/{name}")
async def read_supplier(name: str, db: Session = Depends(get_db)):
    try:
        return crud.get_supplier(db, name=name)
    except:
        raise HTTPException(status_code=404, detail="Supplier not found")
    
@app.get("/suppliers/")
async def read_suppliers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    try:
        return crud.get_suppliers(db, skip=skip, limit=limit)
    except:
        raise HTTPException(status_code=404, detail="Suppliers not found")
    
@app.post("/product/")
async def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_product(db=db, product=product)
    except:
        raise HTTPException(status_code=400, detail="Product already exists")
    
@app.get("/product/{id_prod}")
async def read_product(id_prod: int, db: Session = Depends(get_db)):
    try:
        return crud.get_product(db, id_prod=id_prod)
    except:
        raise HTTPException(status_code=404, detail="Product not found")
    
@app.get("/products/")
async def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    try:
        return crud.get_products(db, skip=skip, limit=limit)
    except:
        raise HTTPException(status_code=404, detail="Products not found")
    
@app.post("/raw_product/")
async def create_raw_product(raw_product: RawProductCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_raw_product(db=db, raw_product=raw_product)
    except:
        raise HTTPException(status_code=400, detail="Raw Product already exists")
    
@app.get("/raw_product/{id_raw}")
async def read_raw_product(id_raw: int, db: Session = Depends(get_db)):
    try:
        return crud.get_raw_product(db, id_raw=id_raw)
    except:
        raise HTTPException(status_code=404, detail="Raw Product not found")
    
@app.get("/raw_products/")
async def read_raw_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    try:
        return crud.get_raw_products(db, skip=skip, limit=limit)
    except:
        raise HTTPException(status_code=404, detail="Raw Products not found")
    
@app.post("/product_recipe/")
async def create_product_recipe(product_recipe: ProductRecipeCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_product_recipe(db=db, product_recipe=product_recipe)
    except:
        raise HTTPException(status_code=400, detail="Product Recipe already exists")
    
@app.get("/product_recipe/{id_prod}/{id_raw}")
async def read_product_recipe(id_prod: int, id_raw: int, db: Session = Depends(get_db)):
    try:
        return crud.get_product_recipe(db, id_prod=id_prod, id_raw=id_raw)
    except:
        raise HTTPException(status_code=404, detail="Product Recipe not found")
    
@app.get("/product_recipes/")
async def read_product_recipes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    try:
        return crud.get_product_recipes(db, skip=skip, limit=limit)
    except:
        raise HTTPException(status_code=404, detail="Product Recipes not found")
    
@app.post("/order/")
async def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_order(db=db, order=order)
    except:
        raise HTTPException(status_code=400, detail="Order already exists")
    
@app.get("/order/{id_order}")
async def read_order(id_order: int, db: Session = Depends(get_db)):
    try:
        return crud.get_order(db, id_order=id_order)
    except:
        raise HTTPException(status_code=404, detail="Order not found")
    
@app.get("/orders/")
async def read_orders(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    try:
        return crud.get_orders(db, skip=skip, limit=limit)
    except:
        raise HTTPException(status_code=404, detail="Orders not found")
    
@app.post("/transaction/")
async def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_transaction(db=db, transaction=transaction)
    except:
        raise HTTPException(status_code=400, detail="Transaction already exists")
    
@app.get("/transaction/{id_supplier}/{id_raw}/{date}")
async def read_transaction(id_supplier: int, id_raw: int, date: str, db: Session = Depends(get_db)):
    try:
        return crud.get_transaction(db, id_supplier=id_supplier, id_raw=id_raw, date=date)
    except:
        raise HTTPException(status_code=404, detail="Transaction not found")
    
@app.get("/transactions/")
async def read_transactions(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    try:
        return crud.get_transactions(db, skip=skip, limit=limit)
    except:
        raise HTTPException(status_code=404, detail="Transactions not found")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
