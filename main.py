from fastapi import FastAPI
import uvicorn

from src.lifespan import lifespan
from src.routes import *


app = FastAPI(lifespan=lifespan)
app.include_router(users_router)


if __name__ == '__main__':
    uvicorn.run(app)
