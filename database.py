from model import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_product(name,brand,price):
	product = Product(
		name = name,
		brand=brand,
		price=price)
	session.add(product)
	session.commit()

def query_by_id(product_id):
    product = session.query(Product).filter_by(id=product_id).first()
    return product

def delete_by_id(product_id):
	session.query(Product).filter_by(id=product_id).delete()
	session.commit()

def query_all():
	products = session.query(Product).all()
	return products
