# ==========================================
# Exercise 7: Bar Chart
# ------------------------------------------
# Create two lists:
#   categories = ['Apples', 'Bananas', 'Cherries']
#   values = [10, 15, 7]
# Use plt.bar() to display a bar chart.
# Add a title and axis labels.

import matplotlib.pyplot as plt
# Define categories and values
categories = ['Apples', 'Bananas', 'Cherries']
values = [10, 15, 7]
# Create bar chart
plt.bar(categories, values)
# Add title and axis labels
plt.title("Fruit Quantities")
plt.xlabel("Fruit Types")
plt.ylabel("Quantity")
# Show the plot

plt.show()
