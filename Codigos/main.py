from fastapi import FastAPI
from app.external.controllers import user_controller
from app.exceptions.exceptions import BusinessException
from app.exceptions.handlers import business_exception_handler

app = FastAPI(title="Finanzas AI")

app.add_exception_handler(BusinessException, business_exception_handler)
app.include_router(user_controller.router, prefix="/api")
