# Exercise 7: Combining Concepts
# -------------------------------
# Ask the user for their age using input().
# Convert it to an integer.
# Print whether they are old enough to vote (18 or older).

# Asking the user for their age
age = input("Please enter your age: ")
# Converting the input to an integer
age = int(age)
# Checking if the user is old enough to vote and printing the result
if age >= 18:
    print("You are old enough to vote.")
else:
    print("You are not old enough to vote.")

    