# python system libs
# external libs
import uvicorn
from fastapi import FastAPI
from loguru import logger
# project import
from config import app_host, app_port
from views.csv_worker import csv_worker_router


logger.add('app.logs', rotation="100 MB", enqueue=True)
app = FastAPI()
app.include_router(csv_worker_router)


if __name__ == "__main__":
    uvicorn.run(app, host=app_host, port=app_port)
