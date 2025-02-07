from fastapi import FastAPI
import uvicorn
from app.routers import SignatureRouter
from app.routers import UserRouter
from app.routers import DeviceRouter
from app.auth import auth

app = FastAPI()
app.include_router(SignatureRouter.router)
app.include_router(UserRouter.router)
app.include_router(DeviceRouter.router)
app.include_router(auth.router)

if __name__=="__main__":
    uvicorn.run("main:app", port=8000, host="0.0.0.0")