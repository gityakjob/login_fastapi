from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise
from pathlib import Path
import os
from datetime import timedelta

os.environ['AUTHJWT_SECRET_KEY'] = os.urandom(24).hex()
os.environ['AUTHJWT_ACCESS_TOKEN_EXPIRES'] = f"{1000000}" # one day
os.environ[']AUTHJWT_REFRESH_TOKEN_EXPIRES'] = f"{7000000}" # seven day

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(
    title="API ISOMI",
    description="API for authentication in ISOMI",
    version="1.0.0",
    openapi_tags=[],
)

origins = [
    "*",
    ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)
from views import *

#declaracion de la base de datos
register_tortoise(
    app,
    db_url=f"sqlite://{BASE_DIR}/db.sqlite3",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
