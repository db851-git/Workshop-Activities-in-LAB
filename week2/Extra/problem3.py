# ======================================
# 3. Organizing Lists
# --------------------------------------
# Create a list of three or more country names.
# Print the list in alphabetical order using sorted().
# Print the original list to show it is unchanged.
# Sort the list permanently using sort() and print it again.
# Print the list in reverse order using reverse().
# Print the number of countries in the list using len().

# Creating a list of three or more country names
countries = ["India", "Brazil", "Australia", "Canada", "Germany"]
# Printing the list in alphabetical order using sorted()
print("Countries in alphabetical order:", sorted(countries))
# Printing the original list to show it is unchanged
print("Original list of countries:", countries)
# Sorting the list permanently using sort() and printing it again
countries.sort()
print("Countries sorted permanently:", countries)
# Printing the list in reverse order using reverse()
countries.reverse()
print("Countries in reverse order:", countries)
# Printing the number of countries in the list using len()
print("Number of countries in the list:", len(countries))
    