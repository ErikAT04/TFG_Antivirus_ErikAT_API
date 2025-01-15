from fastapi import FastAPI
import uvicorn
from controllers import SignatureController

app = FastAPI()
app.include_router(SignatureController.router)

if __name__=="__main__":
    uvicorn.run("main:app", port=8000)