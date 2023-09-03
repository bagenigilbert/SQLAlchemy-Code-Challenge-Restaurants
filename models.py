# Import necessary modules from SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Create a base class for declarative models
Base = declarative_base()

# Define the Restaurant class as a SQLAlchemy model
class Restaurant(Base):
    # Define the name of the database table for this model
    __tablename__ = 'restaurants'

    # Define columns for the restaurants table
    id = Column(Integer, primary_key=True)  # Integer primary key
    name = Column(String)  # String column for restaurant name
    price = Column(Integer)  # Integer column for price

    # Create a relationship with the Review class, linking reviews to restaurants
    reviews = relationship('Review', back_populates='restaurant')

    # Define a method to retrieve customers who have reviewed this restaurant
    def customers(self):
        return [review.customer for review in self.reviews]

    # Define a class method to find the fanciest restaurant using a session
    @classmethod
    def fanciest(cls, session):
        return session.query(cls).order_by(cls.price.desc()).first()

    # Define a method to retrieve all reviews for this restaurant
    def all_reviews(self):
        return [review.full_review() for review in self.reviews]

# Define the Customer class as a SQLAlchemy model
class Customer(Base):
    # Define the name of the database table for this model
    __tablename__ = 'customers'

    # Define columns for the customers table
    id = Column(Integer, primary_key=True)  # Integer primary key
    first_name = Column(String)  # String column for first name
    last_name = Column(String)  # String column for last name

    # Create a relationship with the Review class, linking reviews to customers
    reviews = relationship('Review', back_populates='customer')

    # Define a method to retrieve the full name of the customer
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    # Define a method to find the favorite restaurant of this customer using a session
    def favorite_restaurant(self, session):
        try:
            # Query the highest star rating given by this customer
            highest_rating = session.query(Review.star_rating).filter(Review.customer_id == self.id).order_by(Review.star_rating.desc()).first()
            
            # Find the restaurant with the highest rating
            highest_rating_restaurant = session.query(Restaurant).filter(Restaurant.reviews.any(Review.star_rating == highest_rating[0])).first()
            
            return highest_rating_restaurant
        except NoResultFound:
            return None

    # Define a method to add a new review for this customer
    def add_review(self, session, restaurant, rating):
        new_review = Review(customer=self, restaurant=restaurant, star_rating=rating)
        session.add(new_review)
        session.commit()

    # Define a method to delete all reviews by this customer for a specific restaurant
    def delete_reviews(self, session, restaurant):
        reviews_to_delete = session.query(Review).filter(Review.customer_id == self.id, Review.restaurant_id == restaurant.id).all()
        for review in reviews_to_delete:
            session.delete(review)
        session.commit()

# Define the Review class as a SQLAlchemy model
class Review(Base):
    # Define the name of the database table for this model
    __tablename__ = 'reviews'

    # Define columns for the reviews table
    id = Column(Integer, primary_key=True)  # Integer primary key
    star_rating = Column(Integer)  # Integer column for star rating

    # Define foreign keys to link reviews to restaurants and customers
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))

    # Create relationships with the Restaurant and Customer classes
    restaurant = relationship('Restaurant', back_populates='reviews')
    customer = relationship('Customer', back_populates='reviews')

    # Define a method to generate a full review string
    def full_review(self):
        return f"Review for {self.restaurant.name} by {self.customer.full_name()}: {self.star_rating} stars"

# Database engine and session creation
engine = create_engine('sqlite:///restaurant_reviews.db')  # SQLite database engine
Session = sessionmaker(bind=engine)  # Create a session class bound to the engine
session = Session()  # Create a session instance

# Create tables in the database
Base.metadata.create_all(engine)  # Generate the database schema
