# ======================================
# 4. Avoiding Index Errors
# --------------------------------------
# Try to print an element at an index that doesn’t exist.
# Wrap your code in a try/except block to handle the error gracefully.

# Creating a list with three elements
my_list = [1, 2, 3]
# Attempting to print an element at an index that doesn't exist
try:
    print(my_list[5])  # This will raise an IndexError
except IndexError:
    print("Error: The index you are trying to access does not exist in the list.")


        