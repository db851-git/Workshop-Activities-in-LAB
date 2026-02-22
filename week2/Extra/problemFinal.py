# ======================================
# Final Challenge
# --------------------------------------
# Create a program that:
#   1. Creates a list of favourite movies.
#   2. Prints them sorted alphabetically.
#   3. Loops through and prints each movie with a custom message.
#   4. Creates a tuple of movie ratings (1–5) and prints the average rating.
#   5. Ensures your program follows PEP 8 guidelines.

# Step 1: Creating a list of favourite movies
favourite_movies = ["The Shawshank Redemption", "The Godfather", "Inception", "The Dark Knight", "Pulp Fiction"]
# Step 2: Printing the movies sorted alphabetically
print("Favourite Movies (Sorted Alphabetically):")
for movie in sorted(favourite_movies):

    print(movie)
# Step 3: Looping through and printing each movie with a custom message
print("\nMy Favourite Movies:")
for movie in favourite_movies:

    print(f"I really enjoy watching '{movie}'!")
# Step 4: Creating a tuple of movie ratings (1–5) and printing the
# average rating
movie_ratings = (5, 4, 5, 4, 5)
average_rating = sum(movie_ratings) / len(movie_ratings)
print(f"\nAverage Movie Rating: {average_rating:.2f}")

