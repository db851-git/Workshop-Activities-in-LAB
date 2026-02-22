# =============================
# EXERCISE 8: Arbitrary Arguments
# =============================
# Task: Define a function called make_pizza(*toppings) that prints all the toppings requested.
# Call it with different numbers of arguments.

# Define the function that accepts arbitrary arguments
def make_pizza(*toppings):
    print("Making a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
# Call the function with different numbers of arguments
make_pizza("pepperoni", "mushrooms", "green peppers")
make_pizza("sausage", "olives")

        