from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables, drop_tables
from routes import router as tasks_router



@asynccontextmanager
async def lifespan(app: FastAPI):
     await drop_tables()
     print("Starting up")
     await create_tables()
     print("Base ready")
     yield
     print("Shutting down")


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)

tasks = []
