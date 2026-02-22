# ==========================================
# Final Challenge: Interactive Program
# ------------------------------------------
# Create a small dictionary of menu items with prices, e.g.:
#   menu = {'coffee': 2.5, 'tea': 2.0, 'cake': 3.5}
# Write a program that:
#   * Repeatedly asks the user to enter an item or 'quit' to stop.
#   * If the item exists, print its price.
#   * If not, print "Sorry, we don't have that."
#   * When the user quits, thank them for visiting.

# Create a dictionary of menu items with prices
menu = {
    'coffee': 2.5,
    'tea': 2.0,
    'cake': 3.5
}
# Write a program that repeatedly asks the user to enter an item or 'quit' to stop
while True:

    user_input = input("Please enter an item or 'quit' to exit: ")
    # Check if the user wants to quit
    if user_input.lower() == 'quit':
        print("Thank you for visiting!")
        break  # Exit the loop
    # Check if the item exists in the menu
    elif user_input in menu:
        print(f"The price of {user_input} is ${menu[user_input]:.2f}.")
    else:
        print("Sorry, we don't have that.")


                