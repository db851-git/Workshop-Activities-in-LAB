# ==========================================
# Exercise 4: Scatter Plot
# ------------------------------------------
# Create two lists:
#   x_values = [1, 2, 3, 4, 5]
#   y_values = [2, 3, 5, 7, 11]
# Use plt.scatter() to plot the data.
# Add axis labels and a title.
# Show the plot.

#Taking the imports from problem1.py
import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [2, 3, 5, 7, 11]

plt.scatter(x_values, y_values)
plt.xlabel("x values")
plt.ylabel("y values")
plt.title("Scatter Plot of x vs y")
plt.show()