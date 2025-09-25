import os
from fastapi import APIRouter,Request
from starlette.responses import JSONResponse
from controller.interested_controller import push_interested_property,get_interested_property,delete_interested_property
from models.interested_model import Interested
from utility.security import verify_jwt_token
from dotenv import load_dotenv
load_dotenv()
interested_route = APIRouter()


@interested_route.post("/interested-property")
async def interested_property(request:Request,body:Interested):
    jwt_token = request.headers.get("Authorization")
    if jwt_token is None:
        return JSONResponse({"message":"No JWT token provided"},status_code=401)
    is_token_valid = verify_jwt_token(token=jwt_token,secret_key=os.getenv("SECRET"))
    if is_token_valid is None:
        return JSONResponse({"message":"Invalid JWT token"},status_code=401)
    else:
        property_id = body.property_id
        result = await push_interested_property(user_id=is_token_valid.get('user_id'),property_id=property_id)
        return JSONResponse(content=result.get("message"),status_code=result.get("status_code"))

@interested_route.delete("/interested-property")
async def interested_property(request:Request,body:Interested):
    jwt_token = request.headers.get("Authorization")
    if jwt_token is None:
        return JSONResponse({"message": "No JWT token provided"}, status_code=401)
    is_token_valid = verify_jwt_token(token=jwt_token, secret_key=os.getenv("SECRET"))
    if is_token_valid is None:
        return JSONResponse({"message": "Invalid JWT token"}, status_code=401)
    else:
        property_id = body.property_id
        result = await delete_interested_property(user_id=is_token_valid.get('user_id'), property_id=property_id)
        return JSONResponse(content=result.get("message"), status_code=result.get("status_code"))



@interested_route.get("/interested-properties")
async def interested_properties(request:Request):
    jwt_token = request.headers.get("Authorization")
    if jwt_token is None:
        return JSONResponse({"message": "No JWT token provided"}, status_code=401)
    is_token_valid = verify_jwt_token(token=jwt_token, secret_key=os.getenv("SECRET"))
    if is_token_valid is None:
        return JSONResponse({"message": "Invalid JWT token"}, status_code=401)
    else:
        result  = await get_interested_property(is_token_valid.get('user_id'))
        return JSONResponse(status_code=result.get("status_code"),content=result.get("message"))


