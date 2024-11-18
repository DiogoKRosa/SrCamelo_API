from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from model.database import db
import uvicorn
from routes import userRoute, loginRoute, productRoute
import os

# Instancia a API
app = FastAPI()

app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

app.include_router(userRoute.router)
app.include_router(loginRoute.router)
app.include_router(productRoute.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI"}

if __name__ == '__main__':

    srcamelo_collections = ['users', 'products', 'invoices']
    collections = db.list_collection_names()

    for collection in srcamelo_collections:
        if collection not in collections:
            db.create_collection(collection)

    upload_dir = "uploads"
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)