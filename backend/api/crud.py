from sqlmodel import Session, SQLModel

def create_instance(db: Session, instance: SQLModel):
    db.add(instance)
    db.commit()
    db.refresh(instance)
    return instance
1
def get_instance(db: Session, name: str, instance: SQLModel):
    return db.exec(instance).filter(instance.name == name).first()

def get_instances(db: Session, instance: SQLModel, skip: int = 0, limit: int = 10):
    return db.exec(instance).offset(skip).limit(limit).all()
