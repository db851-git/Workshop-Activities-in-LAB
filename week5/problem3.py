# =============================
# EXERCISE 3: Default Values
# =============================
# Task: Give your function a default value for 'name' (e.g., 'Guest').
# Test calling it with and without providing a name.

# Define the function with a default parameter value
def greet_user(name="Guest"):
    print(f"Hello, {name}! Welcome to the programming world.")
# Call the function without providing a name (uses default value)
greet_user()
# Call the function with a specific name
greet_user("Eve")



