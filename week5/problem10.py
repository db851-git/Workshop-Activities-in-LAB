# =============================
# EXERCISE 10: Modules
# =============================
# Task: Create a separate Python file called 'my_functions.py' with a simple function (e.g., greet_user()).
# Import that function in this script and call it.
# Try importing:
#   - the whole module
#   - a specific function
#   - a function using an alias

# Import the whole module
import my_functions
# Call the function from the module
my_functions.greet_user("DEB")
# Import a specific function
from my_functions import greet_user
# Call the imported function
greet_user("Ram")
# Import the function using an alias
from my_functions import greet_user as greet
# Call the function using the alias
greet("Shyam")


