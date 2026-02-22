# =============================
# EXERCISE 5: Returning a Dictionary
# =============================
# Task: Modify make_full_name() to return a dictionary with keys 'first' and 'last'.
# Print the result.

# Define the function that returns a dictionary with first and last names
def make_full_name(first, last):
    full_name_dict = {
        "first": first,
        "last": last
    }
    return full_name_dict
# Call the function and print the returned dictionary
full_name_info = make_full_name("Grace", "Hopper")
print(f"Full Name Dictionary: {full_name_info}")

    