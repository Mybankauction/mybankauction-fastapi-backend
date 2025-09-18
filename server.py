import fastapi
import uvicorn
import os
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from routes.properties import property_router
from routes.auth import auth_router
from routes.interested import interested_route
from db_config import init_db
from contextlib import asynccontextmanager
@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    print("App starting up...")
    await init_db()
    yield
    # shutdown
    print("App shutting down...")

app = fastapi.FastAPI(lifespan=lifespan)
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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)