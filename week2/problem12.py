# Extra Challenge 4
# -----------------
# Ask the user for their age and whether it is sunny (True/False).
# Print whether they are allowed to go outside if they are at least 12 years old AND it is sunny.

# Asking the user for their age
age = input("Please enter your age: ")
# Converting the age input to an integer
age = int(age)
# Asking the user if it is sunny
is_sunny_input = input("Is it sunny outside? (True/False): ")
# Converting the sunny input to a boolean
is_sunny = is_sunny_input.lower() == "true"
# Checking if the user is allowed to go outside and printing the result
if age >= 12 and is_sunny:
    print("You are allowed to go outside.")
else:
    print("You are not allowed to go outside.")

        