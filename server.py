import secrets
import fastapi
import uvicorn
from starlette.middleware.cors import CORSMiddleware
from routes.properties import property_router
from routes.auth import auth_router
from routes.interested import interested_route
from db_config import init_db
app = fastapi.FastAPI()
app.include_router(property_router)
app.include_router(auth_router)
app.include_router(interested_route)
origins = ["*"]
app.add_middleware(CORSMiddleware,
    allow_origins=origins,        # List of allowed origins
    allow_credentials=True,       # Allow cookies, auth headers
    allow_methods=["*"],          # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],
                   )# Allow all headers)
@app.on_event("startup")
async def startup():
    await init_db()
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
