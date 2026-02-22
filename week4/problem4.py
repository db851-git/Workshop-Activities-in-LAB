# ==========================================
# Exercise 4: Using if with Lists
# ------------------------------------------
# Create a list of fruits = ['apple', 'banana', 'cherry']
# Ask the user to input a fruit name.
# If the fruit is in the list, print "Yes, we have that!"
# Otherwise, print "Sorry, we don't have that."

# Create a list of fruits
fruits = ['apple', 'banana', 'cherry']
# Ask the user to input a fruit name
user_input = input("Please enter a fruit name: ")
# Check if the fruit is in the list
if user_input in fruits:
    print("Yes, we have that!")
else:
    print("Sorry, we don't have that.")


            