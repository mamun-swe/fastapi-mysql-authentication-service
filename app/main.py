from fastapi import FastAPI
from app.api.v1.routes import users
from app.core.error_handlers import register_error_handlers

app = FastAPI()

# Register error handlers
register_error_handlers(app)

# include routers
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])


@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI PgSQL authentication service"}
