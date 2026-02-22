# ======================================
# 2. Modifying Lists
# --------------------------------------
# Change the value of the first fruit in your list.
# Add a new fruit to the end of the list using append().
# Insert a fruit at the beginning using insert().
# Remove one fruit using del, one using pop(), and one using remove().
# Print the updated list.

# Creating a list called fruits with at least three fruit names
fruits = ["Apple", "Banana", "Cherry"]
# Changing the value of the first fruit in the list
fruits[0] = "Mango"
# Adding a new fruit to the end of the list using append()
fruits.append("Orange")
# Inserting a fruit at the beginning using insert()
fruits.insert(0, "Grapes")
# Removing one fruit using del
del fruits[1]  # This will remove "Mango"
# Removing one fruit using pop()
popped_fruit = fruits.pop(2)  # This will remove "Cherry"
# Removing one fruit using remove()
fruits.remove("Orange")  # This will remove "Orange"
# Printing the updated list
print(fruits)


    