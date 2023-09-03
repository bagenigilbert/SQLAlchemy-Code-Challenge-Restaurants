# Import necessary SQLAlchemy classes and functions
from models import Restaurant, Customer, Review, session
from sqlalchemy.orm.exc import NoResultFound

# Check if this script is being run as the main program
if __name__ == "__main__":
    # Create sample data for restaurants, customers, and reviews

    # Create Restaurant objects with name and price attributes
    restaurant1 = Restaurant(name="Restaurant A", price=3)
    restaurant2 = Restaurant(name="Restaurant B", price=2)

    # Create Customer objects with first_name and last_name attributes
    customer1 = Customer(first_name="John", last_name="Doe")
    customer2 = Customer(first_name="Jane", last_name="Smith")

    # Create Review objects with customer, restaurant, and star_rating attributes
    review1 = Review(customer=customer1, restaurant=restaurant1, star_rating=5)
    review2 = Review(customer=customer1, restaurant=restaurant2, star_rating=4)
    review3 = Review(customer=customer2, restaurant=restaurant1, star_rating=3)

    # Add the sample data to the database session and commit the changes
    session.add_all([restaurant1, restaurant2, customer1, customer2, review1, review2, review3])
    session.commit()

    # Get the fanciest restaurant from the database

    # Query the database for the fanciest restaurant
    fanciest_restaurant = Restaurant.fanciest(session)

    # Print the name of the fanciest restaurant
    print(f"Fanciest restaurant: {fanciest_restaurant.name}")

    # Get all reviews for "Restaurant A"

    # Query the database to find the Restaurant A object
    restaurant1 = session.query(Restaurant).filter_by(name="Restaurant A").first()

    # Check if Restaurant A exists
    if restaurant1:
        # Get all reviews for Restaurant A and store them in a list
        reviews_for_restaurant1 = restaurant1.all_reviews()

        # Print a header for the reviews
        print("Reviews for Restaurant A:")

        # Loop through the reviews and print each one
        for review in reviews_for_restaurant1:
            print(review)
    else:
        # Print a message if Restaurant A does not exist
        print("Restaurant A does not exist.")

    # Create a new customer and add them to the database

    # Create a new Customer object with first_name and last_name attributes
    new_customer = Customer(first_name="Alice", last_name="Johnson")

    # Add the new customer to the database session
    session.add(new_customer)

    # Commit the changes to the database
    session.commit()

    # Add a review for a restaurant

    # Query the database to find the Restaurant A object again
    restaurant1 = session.query(Restaurant).filter_by(name="Restaurant A").first()

    # Check if Restaurant A exists
    if restaurant1:
        # Create a new Review object for the new customer's review of Restaurant A
        new_review = Review(customer=new_customer, restaurant=restaurant1, star_rating=4)

        # Add the new review to the database session
        session.add(new_review)

        # Commit the changes to the database
        session.commit()

        # Print a message indicating that the review was added
        print("Added review for Restaurant A")
    else:
        # Print a message if Restaurant A does not exist
        print("Restaurant A does not exist.")

    # Find the favorite restaurant for a customer ("Jane Smith" in this case)

    # Query the database to find the Customer object for Jane Smith
    customer2 = session.query(Customer).filter_by(first_name="Jane").first()

    # Check if Jane Smith exists
    if customer2:
        # Find Jane Smith's favorite restaurant using the favorite_restaurant method
        favorite_restaurant = customer2.favorite_restaurant(session)

        # Check if Jane Smith has a favorite restaurant
        if favorite_restaurant:
            # Print the name of Jane Smith's favorite restaurant
            print(f"Favorite restaurant for Jane Smith: {favorite_restaurant.name}")
        else:
            # Print a message if Jane Smith does not have a favorite restaurant
            print("Jane Smith has not reviewed any restaurants yet.")
    else:
        # Print a message if Jane Smith does not exist
        print("Customer Jane Smith not found.")

    # Delete all reviews by a customer ("John Doe") for a specific restaurant ("Restaurant A")

    # Query the database to find the Customer object for John Doe
    customer1 = session.query(Customer).filter_by(first_name="John").first()

    # Query the database to find the Restaurant A object
    restaurant_to_delete_reviews = session.query(Restaurant).filter_by(name="Restaurant A").first()

    # Check if both the customer and the restaurant exist
    if customer1 and restaurant_to_delete_reviews:
        # Call the delete_reviews method to delete all reviews by John Doe for Restaurant A
        customer1.delete_reviews(session, restaurant_to_delete_reviews)

        # Print a message indicating that the reviews were deleted
        print("Deleted reviews by John Doe for Restaurant A")
    elif not customer1:
        # Print a message if John Doe does not exist
        print("Customer John Doe not found.")
    else:
        # Print a message if Restaurant A does not exist
        print("Restaurant A does not exist.")

    # Check if a customer ("Alice Johnson") has reviewed a restaurant ("Restaurant A")

    # Query the database to find the Customer object for Alice Johnson
    new_customer = session.query(Customer).filter_by(first_name="Alice").first()

    # Query the database to find the Restaurant A object again
    restaurant1 = session.query(Restaurant).filter_by(name="Restaurant A").first()

    # Check if both Alice Johnson and Restaurant A exist
    if new_customer and restaurant1:
        # Query the database to check if Alice Johnson has reviewed Restaurant A
        has_reviewed = session.query(Review).filter(
            Review.customer_id == new_customer.id,
            Review.restaurant_id == restaurant1.id
        ).first() is not None

        # Print a message indicating whether Alice Johnson has reviewed Restaurant A
        if has_reviewed:
            print("Alice Johnson has reviewed Restaurant A.")
        else:
            print("Alice Johnson has not reviewed Restaurant A.")
    elif not new_customer:
        # Print a message if Alice Johnson does not exist
        print("Customer Alice Johnson not found.")
    else:
        # Print a message if Restaurant A does not exist
        print("Restaurant A does not exist.")

    # Get all customers who have reviewed a specific restaurant ("Restaurant B")

    # Query the database to find the Restaurant B object
    restaurant2 = session.query(Restaurant).filter_by(name="Restaurant B").first()

    # Check if Restaurant B exists
    if restaurant2:
        # Use the customers method to get a list of customers who have reviewed Restaurant B
        customers_for_restaurant2 = restaurant2.customers()

        # Print a header for the list of customers
        print("Customers who have reviewed Restaurant B:")

        # Loop through the list of customers and print their full names
        for customer in customers_for_restaurant2:
            print(customer.full_name())
    else:
        # Print a message if Restaurant B does not exist
        print("Restaurant B does not exist.")

    # Update a customer's information ("John Doe" to "Johnathan Doe")

    # Query the database to find the Customer object for John Doe
    customer1 = session.query(Customer).filter_by(first_name="John").first()

    # Check if John Doe exists
    if customer1:
        # Update John Doe's first name to "Johnathan"
        customer1.first_name = "Johnathan"

        # Commit the changes to the database
        session.commit()

        # Print a message indicating that the customer's first name has been updated
        print(f"Updated customer's first name to {customer1.first_name}")
    else:
        # Print a message if John Doe does not exist
        print("Customer John Doe not found.")

    # Get the number of reviews for a restaurant ("Restaurant A" in this case)

    # Query the database to find the Restaurant A object again
    restaurant1 = session.query(Restaurant).filter_by(name="Restaurant A").first()

    # Check if Restaurant A exists
    if restaurant1:
        # Use the count method to get the number of reviews for Restaurant A
        review_count = session.query(Review).filter_by(restaurant_id=restaurant1.id).count()

        # Print the number of reviews for Restaurant A
        print(f"Number of reviews for Restaurant A: {review_count}")
    else:
        # Print a message if Restaurant A does not exist
        print("Restaurant A does not exist.")
