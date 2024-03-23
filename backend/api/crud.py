from sqlmodel import Session, SQLModel, select, delete, update
from schema import RawProduct

def create_instance(db: Session, instance: SQLModel):
    db.add(instance)
    db.commit()
    db.refresh(instance)
    return instance
1
def get_instance(db: Session, parameters: dict, instance: SQLModel):
    statement = select(instance)
    for key, value in parameters.items():
        statement = statement.where(getattr(instance, key) == value)
    
    results = db.exec(statement)
    return results.all()
    
def get_instances(db: Session, instance: SQLModel, llimit: int = 10):
    statement = select(instance).limit(llimit)
    results = db.exec(statement)
    return results.all()

def delete_table(db: Session, table: SQLModel):
    statement = delete(table)
    result = db.exec(statement)
    db.commit()
    
    return result.rowcount

def update_raw_amount(db: Session, id_raw: int, amount: int):
    
    statement = select(RawProduct).where(RawProduct.id_raw == id_raw)
    result = db.exec(statement)
    raw = result.one()
    raw.amount = round(raw.amount + amount, 2)
    
    statement = update(RawProduct).where(RawProduct.id_raw == id_raw).values(amount=raw.amount)
    result = db.exec(statement)
    
    db.commit()
    db.refresh(raw)
    return raw.amount