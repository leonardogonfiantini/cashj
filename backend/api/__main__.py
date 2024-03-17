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
        return crud.get_instance(db, parameters={"name": name}, instance=Category)
    except:
        raise HTTPException(status_code=404, detail="Category not found")

@app.get("/categories/")
async def read_categories(limit: int = 10, db: Session = Depends(get_session)):
    try:
        return crud.get_instances(db, instance=Category, llimit=limit)
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
        return crud.get_instance(db, parameters={"id_supplier": id_supplier}, instance=Supplier)
    except:
        raise HTTPException(status_code=404, detail="Supplier not found")
    
@app.get("/suppliers/")
async def read_suppliers(limit: int = 10, db: Session = Depends(get_session)):
    try:
        return crud.get_instances(db, instance=Supplier, llimit=limit)
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
        return crud.get_instance(db, parameters={"id_prod": id_prod}, instance=Product)
    except:
        raise HTTPException(status_code=404, detail="Product not found")
    
@app.get("/products/")
async def read_products(limit: int = 10, db: Session = Depends(get_session)):
    try:
        return crud.get_instances(db, instance=Product, llimit=limit)
    except:
        raise HTTPException(status_code=404, detail="Products not found")
    
@app.post("/rawproduct/")
async def create_rawproduct(rawproduct: RawProduct, db: Session = Depends(get_session)):
    try:
        return crud.create_instance(db=db, instance=rawproduct)
    except:
        raise HTTPException(status_code=400, detail="RawProduct already exists")
    
@app.get("/rawproduct/{id_raw}")
async def read_rawproduct(id_raw: int, db: Session = Depends(get_session)):
    try:
        return crud.get_instance(db, parameters={"id_raw": id_raw}, instance=RawProduct)
    except:
        raise HTTPException(status_code=404, detail="RawProduct not found")

@app.get("/rawproducts/")
async def read_rawproducts(limit: int = 10, db: Session = Depends(get_session)):
    try:
        return crud.get_instances(db, instance=RawProduct, llimit=limit)
    except:
        raise HTTPException(status_code=404, detail="RawProducts not found")
    
@app.post("/productrecipe/")
async def create_product_recipe(product_recipe: ProductRecipe, db: Session = Depends(get_session)):
    try:
        return crud.create_instance(db=db, instance=product_recipe)
    except:
        raise HTTPException(status_code=400, detail="ProductRecipe already exists")
    
@app.get("/productrecipe/{id_prod}/{id_raw}")
async def read_product_recipe(id_prod: int, id_raw: int, db: Session = Depends(get_session)):
    try:
        return crud.get_instance(db, parameters={"id_prod": id_prod, "id_raw": id_raw}, instance=ProductRecipe)
    except:
        raise HTTPException(status_code=404, detail="ProductRecipe not found")
    
@app.get("/productrecipes/")
async def read_product_recipes(limit: int = 10, db: Session = Depends(get_session)):
    try:
        return crud.get_instances(db, instance=ProductRecipe, llimit=limit)
    except:
        raise HTTPException(status_code=404, detail="ProductRecipes not found")
    
@app.post("/order/")
async def create_order(order: Order, db: Session = Depends(get_session)):
    try:
        return crud.create_instance(db=db, instance=order)
    except:
        raise HTTPException(status_code=400, detail="Order already exists")
    
@app.get("/order/{billNo}")
async def read_order(billNo: int, db: Session = Depends(get_session)):
    try:
        return crud.get_instance(db, parameters={"billNo": billNo}, instance=Order)
    except:
        raise HTTPException(status_code=404, detail="Order not found")
    
@app.get("/orders/")
async def read_orders(limit: int = 10, db: Session = Depends(get_session)):
    try:
        return crud.get_instances(db, instance=Order, llimit=limit)
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
        return crud.get_instance(db, parameters={"id_supplier": id_supplier, "id_raw": id_raw, "date": date}, instance=Transaction)
    except:
        raise HTTPException(status_code=404, detail="Transaction not found")
    
@app.get("/transactions/")
async def read_transactions(limit: int = 10, db: Session = Depends(get_session)):
    try:
        return crud.get_instances(db, instance=Transaction, llimit=limit)
    except:
        raise HTTPException(status_code=404, detail="Transactions not found")

@app.delete("/deletetable/{table}")
async def delete_table(table: str, db: Session = Depends(get_session)):
    try:
        match table:
            case "category":
                return crud.delete_table(db, Category)
            case "supplier":
                return crud.delete_table(db, Supplier)
            case "product":
                return crud.delete_table(db, Product)
            case "rawproduct":
                return crud.delete_table(db, RawProduct)
            case "productrecipe":
                return crud.delete_table(db, ProductRecipe)
            case "order":
                return crud.delete_table(db, Order)
            case "transaction":
                return crud.delete_table(db, Transaction)
            case _:
                raise HTTPException(status_code=404, detail="Table not found")
    except:
        raise HTTPException(status_code=404, detail="Table not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
