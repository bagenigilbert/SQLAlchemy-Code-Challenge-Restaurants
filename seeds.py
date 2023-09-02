from models import Restaurant, Customer, Review, session

# Create sample data
restaurant1 = Restaurant(name="Restaurant A", price=3)
restaurant2 = Restaurant(name="Restaurant B", price=2)

customer1 = Customer(first_name="John", last_name="Doe")
customer2 = Customer(first_name="Jane", last_name="Smith")

review1 = Review(customer=customer1, restaurant=restaurant1, star_rating=5)
review2 = Review(customer=customer1, restaurant=restaurant2, star_rating=4)
review3 = Review(customer=customer2, restaurant=restaurant1, star_rating=3)

# Add data to the session and commit
session.add_all([restaurant1, restaurant2, customer1, customer2, review1, review2, review3])
session.commit()
