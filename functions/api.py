import os
from fastapi import FastAPI
from mangum import Mangum

# Importa tu aplicación FastAPI
from api.main import app

# Crea un adaptador para AWS Lambda
handler = Mangum(app)

def lambda_handler(event, context):
    return handler(event, context)