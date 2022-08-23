from fastapi import FastAPI

app  = FastAPI(docs_url='/docs', redoc_url='/redoc')

from routers.supplier.main import router as supplier

app.include_router(supplier, tags=['suppliers'])