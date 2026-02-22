# =============================
# EXERCISE 9: Arbitrary Keyword Arguments
# =============================
# Task: Define a function called build_profile(first, last, **info) that stores any number of keyword-value pairs.
# Test it with different pieces of user data.


# Define the function that accepts arbitrary keyword arguments
def build_profile(first, last, **info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in info.items():
        profile[key] = value
    return profile
# Test the function with different pieces of user data
user_profile = build_profile("Grace", "Hopper", location="USA", field="ComputerScience")
print(f"User Profile: {user_profile}")
    
