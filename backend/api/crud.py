from sqlmodel import Session, SQLModel, select, delete

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