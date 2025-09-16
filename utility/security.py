import bcrypt
import jwt

def get_hashed_password(password):
    password = password.encode('utf-8')
    return bcrypt.hashpw(password, bcrypt.gensalt(rounds=12)).decode('utf-8')

def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

def generate_jwt_token(secret_key,data):
    JWT_ALGORITHM = "HS256"
    token = jwt.encode(data,secret_key,JWT_ALGORITHM)
    print(token)
    return token

def verify_jwt_token(secret_key,token):
    JWT_ALGORITHM = "HS256"
    try:
        is_token_valid = jwt.decode(token,secret_key,algorithms=[JWT_ALGORITHM])
        return is_token_valid
    except jwt.InvalidTokenError:
        return None