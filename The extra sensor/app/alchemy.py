# coding: utf-8
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Family(Base):
    __tablename__ = 'family'

    id = Column(Integer, primary_key=True)
    name = Column(String(85))
    gender = Column(String(85))
    sexuality = Column(String(85))
    disability = Column(String(85))


class HeatingProfile(Base):
    __tablename__ = 'heating_profiles'

    id = Column(Integer, primary_key=True)
    name = Column(String(85))
    temp = Column(Integer)


class HomeSetting(Base):
    __tablename__ = 'home_settings'

    param = Column(String(20), primary_key=True)
    value = Column(String(45), nullable=False)
