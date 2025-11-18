from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
router = APIRouter()

class LoginIn(BaseModel):
    email: str
    password: str

@router.post("/login")
def login(body: LoginIn):
    # demo stub: accept any login and return fake token
    if not body.email:
        raise HTTPException(400,"missing email")
    return {"token":"demo-token","user":{"email":body.email,"role":"tenant"}}
