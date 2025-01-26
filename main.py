from fastapi import FastAPI
import uvicorn
from app.routers import SignatureRouter
from app.routers import UserRouter
from app.routers import DeviceRouter

app = FastAPI()
app.include_router(SignatureRouter.router)
app.include_router(UserRouter.router)
app.include_router(DeviceRouter.router)


uvicorn.run("main:app", port=8000)