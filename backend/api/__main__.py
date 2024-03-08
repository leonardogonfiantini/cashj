from contextlib import asynccontextmanager
from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app: FastAPI):
    #connect to database
    await app.state.database.connect()
    try:
        yield
    finally:
        await app.state.database.disconnect()    
    
app = FastAPI(lifespan=lifespan)

from models import User
from typing import List, Optional

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/user/{user_id}")
async def read_user(user_id: int, q: Optional[str] = None):
    return await User.objects.get(id=user_id)

@app.put("/user/{user_id}")
async def update_user(user: User):
    await user.save()
    return user

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
