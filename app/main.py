from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import  user, auth,data, post
from .config import settings


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# origins = ["http://localhost:4200"]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

app.include_router(user.router)
app.include_router(auth.router)
app.include_router(data.router)
app.include_router(post.router)

