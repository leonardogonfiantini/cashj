import ormar
from database import metadata, database

class User(ormar.Model):
    class Meta:
        tablename = "users"
        metadata = metadata
        database = database
        
    id = ormar.Integer(primary_key=True)
    username = ormar.String(max_length=100)
    email = ormar.String(max_length=100)
    password = ormar.String(max_length=100)
    

    