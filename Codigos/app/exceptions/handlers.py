from fastapi.responses import JSONResponse
from fastapi import Request
from .exceptions import BusinessException

async def business_exception_handler(request: Request, exc: BusinessException):
    return JSONResponse(
        status_code=400,
        content={
            "status_code": 400,
            "error": exc.code.name,  
            "detail": exc.code.value  
        },
    )
