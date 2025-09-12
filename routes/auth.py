
from fastapi import APIRouter
from starlette.responses import JSONResponse
from models.login_model import User
from models.register_model import Register
from controller.auth_controller import register_user,login
auth_router = APIRouter()


@auth_router.post("/register")
async def register_new_user(register: Register):
    result = await register_user(register)
    return JSONResponse(status_code=result.get("status_code"),content=result.get("message"))



@auth_router.post("/login")
async def login_user(user: User):
    result = await login(user)
    return JSONResponse(status_code=result.get("status_code"),content=result.get("message"))



