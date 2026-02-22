# ==========================================
# Exercise 14: while Loops with Lists
# ------------------------------------------
# Create a list of unconfirmed_users = ['alice', 'bob', 'charlie']
# and an empty list confirmed_users = []
# Use a while loop to move each user from unconfirmed_users to confirmed_users.
# Print messages confirming each user has been verified.

# Create a list of unconfirmed_users
unconfirmed_users = ['alice', 'bob', 'charlie']
# Create an empty list for confirmed_users
confirmed_users = []
# Use a while loop to move each user from unconfirmed_users to confirmed_users
while unconfirmed_users:
    # Remove the last user from unconfirmed_users
    current_user = unconfirmed_users.pop()
    # Simulate confirming the user (you could add more logic here if needed)
    print(f"Confirming user: {current_user}")
    # Add the confirmed user to confirmed_users
    confirmed_users.append(current_user)
# Print the list of confirmed users
print("The following users have been confirmed:")
for user in confirmed_users:
    print(user)

            