# Extra Challenge 1
# -----------------
# Ask the user for their name and age.
# Print a message: "Hello <name>, you will be <age+1> next year."

# Asking the user for their name and age
name = input("Please enter your name: ")
age = input("Please enter your age: ")
# Converting the age input to an integer
age = int(age)
# Calculating the age next year
age_next_year = age + 1
# Printing the message with the user's name and age next year
print(f"Hello {name}, you will be {age_next_year} next year.")

    