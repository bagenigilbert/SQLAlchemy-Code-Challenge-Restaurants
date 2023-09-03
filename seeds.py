# Import necessary classes and session from models.py
from models import Restaurant, Customer, Review, session

# Create sample data for restaurants, customers, and reviews

# Create two restaurant objects with names and prices
restaurant1 = Restaurant(name="Restaurant A", price=3111)
restaurant2 = Restaurant(name="Restaurant B", price=2000)

# Create two customer objects with first names and last names
customer1 = Customer(first_name="gilbert", last_name="Doe")
customer2 = Customer(first_name="evans", last_name="Smith")

# Create three review objects associating customers with restaurants and providing star ratings
review1 = Review(customer=customer1, restaurant=restaurant1, star_rating=5)
review2 = Review(customer=customer1, restaurant=restaurant2, star_rating=4)
review3 = Review(customer=customer2, restaurant=restaurant1, star_rating=3)

# Add all created objects to the session to prepare them for database insertion
session.add_all([restaurant1, restaurant2, customer1, customer2, review1, review2, review3])

# Commit the changes to the database to persist the sample data
session.commit()
