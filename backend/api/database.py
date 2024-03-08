import databases
import sqlalchemy
from __main__ import app

import os 
db_uri = os.environ.get('POSTGRES_URL')

metadata = sqlalchemy.MetaData()
database = databases.Database(db_uri)
app.state.database = database
