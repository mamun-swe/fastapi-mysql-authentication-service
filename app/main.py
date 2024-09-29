from fastapi import FastAPI
from app.api.v1.routes import users
from app.core.error_handlers import register_error_handlers
from app.core.database import get_db, database

# Define the FastAPI application
app = FastAPI()


# Register database connection
@app.on_event("startup")
async def startup():
    try:
        await database.connect()
        print("Database connection successful")
    except Exception as e:
        print(f"Database connection failed: {e}")


# Register database disconnection
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


# Register error handlers
register_error_handlers(app)

# include routers
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])


# Handle root route
@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI PgSQL authentication service"}
