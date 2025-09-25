import os
from models.register_model import RegisterDb
from models.login_model import LoginModel
from utility.security import get_hashed_password,verify_password,generate_jwt_token
import dotenv
dotenv.load_dotenv()
async def register_user(register):
    #first check if the email id is already exists or not
    try:
      user = await RegisterDb.find_one({"email":register.email})
    except Exception as e:
        print("Error happend at register_user",e)
        return{"status_code":500,"message":"Internal server error"}
    if not user:
        #hash a password and store it in the db
        hashed_password = get_hashed_password(register.password)
        new_user = RegisterDb(
            full_name=register.full_name,
            email=register.email,
            hashed_password=hashed_password,
            phone_number=register.phone_number,
        )
        try:
            insertion_result = await new_user.insert()
            return {"status_code":201, "message":"User registered successfully"}
        except Exception as e:
            print("Error happend at register_user",e)
            return {"status_code":500,"message":"Internal server error"}
    else:
        return {"status_code":409, "message":"User already registered try to login"}

async def login(user):
    #check wheather the user is already existing in the db or not
    email = user.email
    password = user.password
    try:
         new_user = LoginModel(email=email,hashed_password='')
         is_user = await new_user.find_one({"email":email})
         if not is_user:
             return {"status_code":401, "message":"user not found pls register"}
         else:
             hashed_password = is_user.hashed_password
             is_password_correct = verify_password(password,hashed_password)
             if is_password_correct:
                 user_dict = is_user.model_dump()
                 obj_id = user_dict["id"]
                 token = generate_jwt_token(os.getenv("SECRET"),{"user_id":str(obj_id)})
                 print(token)
                 return {"status_code":200,"message":{"login_success_message":True,"token":token,"user_profile":{"email":user_dict.get('email'),"full_name":user_dict.get('full_name'),"phone_number":user_dict.get('phone_number')}}}
             else:
                 return {"status_code":401, "message":"Incorrect password"}
    except Exception as e:
     print("Error happend at login",e)
     return {"status_code":500,"message":"Internal server error"}


