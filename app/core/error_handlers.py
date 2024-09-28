from fastapi import Request, FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from starlette.responses import JSONResponse


# Custom validation error handler
async def validation_error_handler(request: Request, exc: RequestValidationError):
    errors = {}
    for error in exc.errors():
        field = error["loc"][-1]
        message = error["msg"]
        # If message starts with "Value error, ", remove it
        if message.startswith("Value error, "):
            message = message.replace("Value error, ", "")

        # Add error message to errors dictionary
        if field not in errors:
            errors[field] = []
        errors[field].append(message)

    return JSONResponse(
        status_code=422,
        content={"status": False, "errors": errors},
    )


# Custom error handlers for 404 errors
def not_found_error_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "status": False,
            "errors": [{"message": exc.detail}],
        },
    )


# Custom error handlers for 500 errors
def server_error_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"status": False, "errors": [{"message": "Something going wrong."}]},
    )


# Register custom error handlers globally
def register_error_handlers(app: FastAPI):
    app.add_exception_handler(RequestValidationError, validation_error_handler)
    app.add_exception_handler(HTTPException, not_found_error_handler)
    app.add_exception_handler(Exception, server_error_handler)
