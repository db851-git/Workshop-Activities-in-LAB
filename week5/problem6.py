# =============================
# EXERCISE 6: Working with Lists
# =============================
# Task: Define a function called print_models(models_to_print) that loops through and prints each model name.
# Pass in a list of model names. Observe how lists behave when passed to functions.

# Define the function that prints each model name from the list
def print_models(models_to_print):
    for model in models_to_print:
        print(f"Model: {model}")
# Create a list of model names
model_names = ["Model A", "Model B", "Model C"]
# Call the function with the list of model names
print_models(model_names)

    