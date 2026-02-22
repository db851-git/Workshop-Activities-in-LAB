# =============================
# EXERCISE 2: Passing Arguments
# =============================
# Task: Modify greet_user() so it accepts one parameter 'name' and prints a personalized greeting.
# Call it using both positional and keyword arguments.

# Define the function with a parameter
def greet_user(name):
    print(f"Hello, {name}! Welcome to the programming world.")
# Call the function using positional arguments
greet_user("Charlie")
# Call the function using keyword arguments
greet_user(name="Diana")

        