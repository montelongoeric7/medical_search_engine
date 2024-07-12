from app.dbs.database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))

class Information(Base):
    __tablename__ = "information"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='TRUE', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    owner = relationship("User")


class Clinic(Base):
    __tablename__="clinics"
    id=Column(Integer,primary_key=True,nullable=False)
    name=Column(String,nullable=False)
    address=Column(String,nullable=False)
    phone=Column(String,nullable=False)
    email=Column(String,nullable=False)
    website=Column(String,nullable=False)
    services=Column(String,nullable=False)
    insurance=Column(String,nullable=False)
    cash=Column(Boolean,nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text("now()"))

