from sqlalchemy import Column, Integer, String
from .db import Base

class Tenant(Base):
    __tablename__ = "tenants"
    id = Column(Integer, primary_key=True, index=True)
    tenant_name = Column(String, index=True)
    type = Column(String)
    client_id_enc = Column(String)
    client_secret_enc = Column(String)
    tenant_id = Column(String, nullable=True)
    delegated_user = Column(String, nullable=True)
    admin_email = Column(String, nullable=True)
