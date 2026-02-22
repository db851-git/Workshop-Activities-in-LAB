# Final Project: Mini Program
# ----------------------------
# Create a simple program that:
#   1. Asks the user for their name and greets them.
#   2. Asks for their age and tells them if they can vote.
#   3. Asks for two numbers and shows their sum, difference, product, and quotient.
#   4. Prints a farewell message that includes their name.

# Step 1: Ask the user for their name and greet them
name = input("Please enter your name: ")
# Greeting the user with their name
print(f"Hello, {name}! Welcome to the mini program.")
# Step 2: Ask for their age and tell them if they can vote
age = input("Please enter your age: ")
# Converting the age input to an integer
age = int(age)
# Checking if the user is old enough to vote and printing the result
if age >= 18:
    print("You are old enough to vote.")
else:
    print("You are not old enough to vote.")
# Step 3: Ask for two numbers and show their sum, difference, product, and
# quotient
num1 = input("Please enter the first number: ")
num2 = input("Please enter the second number: ")
# Converting the inputs to integers

num1 = int(num1)
num2 = int(num2)
# Calculating the sum, difference, product, and quotient
sum = num1 + num2
difference = num1 - num2
product = num1 * num2
# Checking if the second number is not zero before calculating the quotient
if num2 != 0:
    quotient = num1 / num2
else:
    quotient = "undefined (cannot divide by zero)"
# Printing the results
print(f"The sum of {num1} and {num2} is: {sum}")
print(f"The difference between {num1} and {num2} is: {difference}")
print(f"The product of {num1} and {num2} is: {product}")
print(f"The quotient of {num1} and {num2} is: {quotient}")
# Step 4: Print a farewell message that includes their name
print(f"Thank you for using the mini program, {name}! Goodbye!")
