from sqlalchemy import Column, Integer, String, Boolean,ForeignKey, Unicode
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Product(Base):
	__tablename__ = 'product'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	brand = Column(String)
	price = Column(String) # Pay attention this is a String. change if needed.
