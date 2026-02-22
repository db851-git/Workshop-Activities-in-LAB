# ==========================================
# Exercise 5: Customizing Plots
# ------------------------------------------
# Create a scatter plot again but:
#   * Use a custom color (e.g., 'green')
#   * Set point size to 100
#   * Add a grid to the chart
#   * Add a title: "Prime Numbers Growth"

import matplotlib.pyplot as plt
#taking values of x and y
x_values = [1, 2, 3, 4, 5]
y_values = [2, 3, 5, 7, 11]
#creating a scatter plot with custom color and size
plt.scatter(x_values, y_values, color='green', s=100)
#adding labels, title and grid
plt.xlabel("x values")
plt.ylabel("y values")
#plt.title("Scatter Plot of x vs y")
plt.title("Prime Numbers Growth")
plt.grid()
#showing the plot
plt.show()
    