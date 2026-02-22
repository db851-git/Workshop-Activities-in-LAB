# Extra Challenge 2
# -----------------
# Ask the user for a number.
# Print whether the number is even or odd.

# Asking the user for a number
number = input("Please enter a number: ")
# Converting the input to an integer
number = int(number)
# Checking if the number is even or odd and printing the result
if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")
        