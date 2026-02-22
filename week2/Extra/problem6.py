# ======================================
# 6. Numerical Lists
# --------------------------------------
# Use range() to generate a list of numbers from 1 to 10.
# Print each number using a for loop.
# Create a list of even numbers between 2 and 20 using range().
# Use min(), max(), and sum() to print statistics about your list.

# Using range() to generate a list of numbers from 1 to 10
numbers = list(range(1, 11))
# Printing each number using a for loop
for number in numbers:
    print(number)
# Creating a list of even numbers between 2 and 20 using range()
even_numbers = list(range(2, 21, 2))
# Using min(), max(), and sum() to print statistics about the list of even numbers
print("Even numbers between 2 and 20:", even_numbers)
print("Minimum even number:", min(even_numbers))
print("Maximum even number:", max(even_numbers))
print("Sum of even numbers:", sum(even_numbers))

    