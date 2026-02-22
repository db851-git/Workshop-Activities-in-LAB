# Exercise 8: Challenge
# ---------------------
# Ask the user for two numbers.
# Print:
#   - Their sum
#   - Whether the first number is greater than the second
#   - Whether the numbers are equal

# Asking the user for two numbers
num1 = input("Please enter the first number: ")
num2 = input("Please enter the second number: ")
# Converting the inputs to integers
num1 = int(num1)
num2 = int(num2)
# Calculating and printing the sum
sum = num1 + num2
print("The sum of the two numbers is:", sum)
# Checking if the first number is greater than the second and printing the result
if num1 > num2:
    print(f"The first number {num1} is greater than the second number {num2}.")
else:    
    print(f"The first number {num1} is not greater than the second number {num2}.")
# Checking if the numbers are equal and printing the result
if num1 == num2:
    print("The numbers are equal.")
else:
    print("The numbers are not equal.")

    
