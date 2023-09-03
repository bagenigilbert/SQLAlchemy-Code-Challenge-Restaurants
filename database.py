from sqlalchemy import create_engine
from models import Restaurant, Customer, Review, session

engine = create_engine('sqlite:///restaurant_reviews.db')
Session = sessionmaker(bind=engine)
session = Session()
