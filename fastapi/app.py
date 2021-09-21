from fastapi import FastAPI
from routes.user import user

app = FastAPI(
    title="My first Api",
    description="api de prueba",
    version="0.0.1",
    openapi_tags=[{
        "name": "users",
        "description": "user routes"
    }]
)
app.include_router(user)
