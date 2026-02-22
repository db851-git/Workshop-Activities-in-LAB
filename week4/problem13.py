# ==========================================
# Exercise 13: Using Flags and break
# ------------------------------------------
# Modify the previous exercise using a flag (e.g., active = True).
# Inside the loop, if the user types 'quit', set active = False to stop the loop.

# Initialize the flag
active = True
# Write a while loop that continues until the user types 'quit'
while active:
    # Ask the user for input
    user_input = input("Please enter a message (type 'quit' to exit): ")
    # Check if the user wants to quit
    if user_input.lower() == 'quit':
        print("Goodbye!")
        active = False  # Set the flag to False to exit the loop
    else:
        print(f"You said: {user_input}")
            