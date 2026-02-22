# ======================================
# 8. Slicing Lists
# --------------------------------------
# Create a list of your favourite foods.
# Print the first three items, middle three items, and last three items using slices.
# Loop through a slice of the list (e.g., first three items) and print each item.
# Make a copy of the list using slicing and modify one of them.

# Creating a list of favourite foods
favourite_foods = ["Pizza", "Sushi", "Burger", "Pasta",
                     "Ice Cream", "Salad", "Tacos", "Steak"]
# Printing the first three items using slices
print("First three items:", favourite_foods[:3])
# Printing the middle three items using slices
print("Middle three items:", favourite_foods[3:6])
# Printing the last three items using slices
print("Last three items:", favourite_foods[-3:])
# Looping through a slice of the list (first three items) and printing each item
print("Looping through the first three items:")
for food in favourite_foods[:3]:
    print(food)
# Making a copy of the list using slicing and modifying one of them
favourite_foods_copy = favourite_foods[:]
favourite_foods_copy.append("Fries")
# Printing both lists to show they are different
print("Original list of favourite foods:", favourite_foods)
print("Modified copy of favourite foods:", favourite_foods_copy)


            