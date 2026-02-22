# ==========================================
# Exercise 11: Using int() and Modulo Operator
# ------------------------------------------
# Ask the user for a number using input().
# Convert it to an integer.
# If the number is even, print "That’s an even number!"
# Otherwise, print "That’s an odd number!"

# Ask the user for a number
user_input = input("Please enter a number: ")
# Convert it to an integer
number = int(user_input)
# Check if the number is even or odd using the modulo operator
if number % 2 == 0:
    print("That’s an even number!")
else:
    print("That’s an odd number!")

        