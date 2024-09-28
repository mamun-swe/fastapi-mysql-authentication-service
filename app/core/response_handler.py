from fastapi.responses import JSONResponse
from app.schemas.response import ResponseModel
from typing import Any


def success_response(
    http_status_code, data: Any, message: str = "Request was successful"
) -> JSONResponse:
    response = ResponseModel(status=True, message=message, data=data)
    return JSONResponse(
        content=response.model_dump(), status_code=http_status_code or 200
    )
