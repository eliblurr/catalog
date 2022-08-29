from fastapi import FastAPI

app  = FastAPI(docs_url='/docs', redoc_url='/redoc')

from routers.supplier.main import router as supplier
from routers.catalog.main import router as catalog
from routers.category.main import router as category
from routers.product.main import router as product

app.include_router(supplier, tags=['Suppliers'])
app.include_router(catalog, tags=['Catalogs'])
app.include_router(category, tags=['Categories'])
app.include_router(product, tags=['Products'])