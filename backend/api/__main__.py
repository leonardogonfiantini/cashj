from fastapi import FastAPI, HTTPException, Depends
from sqlmodel import Session, SQLModel
from database import engine

import crud
from schema import Category, Supplier, Product, RawProduct, ProductRecipe, Order, Transaction
        
def get_session():
    with Session(engine) as session:
        yield session    
    
app = FastAPI()
SQLModel.metadata.create_all(engine)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/category/")
async def create_category(category: Category, db: Session = Depends(get_session)):
    try:
        return crud.create_instance(db=db, instance=category)
    except:
        raise HTTPException(status_code=400, detail="Category already exists")

@app.get("/category/{name}")
async def read_category(name: str, db: Session = Depends(get_session)):
    try:
        return crud.get_instance(db, name=name, instance=Category)
    except:
        raise HTTPException(status_code=404, detail="Category not found")

@app.get("/categories/")
async def read_categories(skip: int = 0, limit: int = 10, db: Session = Depends(get_session)):
    try:
        return crud.get_instances(db, instance=Category, skip=skip, limit=limit)
    except:
        raise HTTPException(status_code=404, detail="Categories not found")
    
@app.post("/supplier/")
async def create_supplier(supplier: Supplier, db: Session = Depends(get_session)):
    try:
        return crud.create_instance(db=db, instance=supplier)
    except:
        raise HTTPException(status_code=400, detail="Supplier already exists")
    
@app.get("/supplier/{id_supplier}")
async def read_supplier(id_supplier: int, db: Session = Depends(get_session)):
    try:
        return crud.get_instance(db, name=id_supplier, instance=Supplier)
    except:
        raise HTTPException(status_code=404, detail="Supplier not found")
    
@app.get("/suppliers/")
async def read_suppliers(skip: int = 0, limit: int = 10, db: Session = Depends(get_session)):
    try:
        return crud.get_instances(db, instance=Supplier, skip=skip, limit=limit)
    except:
        raise HTTPException(status_code=404, detail="Suppliers not found")
    
@app.post("/product/")
async def create_product(product: Product, db: Session = Depends(get_session)):
    try:
        return crud.create_instance(db=db, instance=product)
    except:
        raise HTTPException(status_code=400, detail="Product already exists")
    
@app.get("/product/{id_prod}")
async def read_product(id_prod: int, db: Session = Depends(get_session)):
    try:
        return crud.get_instance(db, name=id_prod, instance=Product)
    except:
        raise HTTPException(status_code=404, detail="Product not found")
    
@app.get("/products/")
async def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_session)):
    try:
        return crud.get_instances(db, instance=Product, skip=skip, limit=limit)
    except:
        raise HTTPException(status_code=404, detail="Products not found")
    
@app.post("/raw_product/")
async def create_raw_product(raw_product: RawProduct, db: Session = Depends(get_session)):
    try:
        return crud.create_instance(db=db, instance=raw_product)
    except:
        raise HTTPException(status_code=400, detail="Raw Product already exists")
    
@app.get("/raw_product/{id_raw}")
async def read_raw_product(id_raw: int, db: Session = Depends(get_session)):
    try:
        return crud.get_instance(db, name=id_raw, instance=RawProduct)
    except:
        raise HTTPException(status_code=404, detail="Raw Product not found")
    
@app.get("/raw_products/")
async def read_raw_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_session)):
    try:
        return crud.get_instances(db, instance=RawProduct, skip=skip, limit=limit)
    except:
        raise HTTPException(status_code=404, detail="Raw Products not found")

@app.post("/product_recipe/")
async def create_product_recipe(product_recipe: ProductRecipe, db: Session = Depends(get_session)):
    try:
        return crud.create_instance(db=db, instance=product_recipe)
    except:
        raise HTTPException(status_code=400, detail="Product Recipe already exists")
    
@app.get("/product_recipe/{id_prod}/{id_raw}")
async def read_product_recipe(id_prod: int, id_raw: int, db: Session = Depends(get_session)):
    try:
        return crud.get_instance(db, name=id_prod, instance=ProductRecipe)
    except:
        raise HTTPException(status_code=404, detail="Product Recipe not found")
    
@app.get("/product_recipes/")
async def read_product_recipes(skip: int = 0, limit: int = 10, db: Session = Depends(get_session)):
    try:
        return crud.get_instances(db, instance=ProductRecipe, skip=skip, limit=limit)
    except:
        raise HTTPException(status_code=404, detail="Product Recipes not found")
    
@app.post("/order/")
async def create_order(order: Order, db: Session = Depends(get_session)):
    try:
        return crud.create_instance(db=db, instance=order)
    except:
        raise HTTPException(status_code=400, detail="Order already exists")
    
@app.get("/order/{billNo}")
async def read_order(billNo: int, db: Session = Depends(get_session)):
    try:
        return crud.get_instance(db, name=billNo, instance=Order)
    except:
        raise HTTPException(status_code=404, detail="Order not found")
    
@app.get("/orders/")
async def read_orders(skip: int = 0, limit: int = 10, db: Session = Depends(get_session)):
    try:
        return crud.get_instances(db, instance=Order, skip=skip, limit=limit)
    except:
        raise HTTPException(status_code=404, detail="Orders not found")
    
@app.post("/transaction/")
async def create_transaction(transaction: Transaction, db: Session = Depends(get_session)):
    try:
        return crud.create_instance(db=db, instance=transaction)
    except:
        raise HTTPException(status_code=400, detail="Transaction already exists")
    
@app.get("/transaction/{id_supplier}/{id_raw}/{date}")
async def read_transaction(id_supplier: int, id_raw: int, date: str, db: Session = Depends(get_session)):
    try:
        return crud.get_instance(db, name=id_supplier, instance=Transaction)
    except:
        raise HTTPException(status_code=404, detail="Transaction not found")
    
@app.get("/transactions/")
async def read_transactions(skip: int = 0, limit: int = 10, db: Session = Depends(get_session)):
    try:
        return crud.get_instances(db, instance=Transaction, skip=skip, limit=limit)
    except:
        raise HTTPException(status_code=404, detail="Transactions not found")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
