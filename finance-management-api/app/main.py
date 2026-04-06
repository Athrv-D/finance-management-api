from fastapi import FastAPI
from app.api import auth,users,records,dashboard

app = FastAPI(title="Finance Backened")


app.include_router(auth.router,prefix="/auth")
app.include_router(users.router,prefix="/users")
app.include_router(records.router,prefix="/records")
app.include_router(dashboard.router,prefix="/dashboard")


@app.get('/')
def root():
    return{"message":"API running"}

from app.db.init_db import init_db


init_db()