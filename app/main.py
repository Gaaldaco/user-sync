from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .db import init_db, SessionLocal
from .models import Tenant
from .encryptor import encrypt_data

app = FastAPI()

class TenantCreate(BaseModel):
    tenant_name: str
    type: str
    client_id: str
    client_secret: str
    tenant_id: str = None
    delegated_user: str = None
    admin_email: str = None

@app.on_event("startup")
def startup():
    init_db()

@app.post("/tenants")
def add_tenant(t: TenantCreate):
    db = SessionLocal()
    try:
        enc_id = encrypt_data(t.client_id)
        enc_secret = encrypt_data(t.client_secret)
        tenant = Tenant(
            tenant_name=t.tenant_name,
            type=t.type,
            client_id_enc=enc_id,
            client_secret_enc=enc_secret,
            tenant_id=t.tenant_id,
            delegated_user=t.delegated_user,
            admin_email=t.admin_email
        )
        db.add(tenant)
        db.commit()
        return {"status": "added"}
    finally:
        db.close()
