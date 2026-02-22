# =============================
# EXERCISE 7: Preventing Modification
# =============================
# Task: Modify print_models() to work on a *copy* of the list so the original is not changed.
# Hint: Pass models_to_print[:] to the function.


# Define the function that prints each model name from a copy of the list
def print_models(models_to_print):
    for model in models_to_print:
        print(f"Model: {model}")
# Create a list of model names
model_names = ["Model A", "Model B", "Model C"]
# Call the function with a copy of the list of model names
print_models(model_names[:])
# Print the original list to show it has not been modified
print(f"Original Model Names: {model_names}")

    