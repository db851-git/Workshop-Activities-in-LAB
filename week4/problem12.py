# ==========================================
# Exercise 12: while Loops
# ------------------------------------------
# Write a while loop that asks for input repeatedly until the user types 'quit'.
# Echo back each message they type (except 'quit').

# Write a while loop that continues until the user types 'quit'
while True:
    # Ask the user for input
    user_input = input("Please enter a message (type 'quit' to exit): ")
    # Check if the user wants to quit
    if user_input.lower() == 'quit':
        print("Goodbye!")
        break  # Exit the loop
    else:
        print(f"You said: {user_input}")


            