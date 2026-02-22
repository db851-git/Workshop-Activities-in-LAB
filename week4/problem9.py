# ==========================================
# Exercise 9: Nesting - Dictionaries in Dictionaries
# ------------------------------------------
# Create a dictionary users = {
#     'alice': {'age': 25, 'city': 'London'},
#     'bob': {'age': 30, 'city': 'New York'}
# }
# Loop through the dictionary and print each user's name and details.

# Create a dictionary users
users = {
    'alice': {'age': 25, 'city': 'London'},
    'bob': {'age': 30, 'city': 'New York'}
}
# Loop through the dictionary and print each user's name and details
for username, details in users.items():
    print(f"Username: {username}")
    print(f"  Age: {details['age']}")
    print(f"  City: {details['city']}")

            