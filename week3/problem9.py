# ==========================================
# Final Challenge: Combining Skills
# ------------------------------------------
# Create a list of 20 x-values (1 to 20) and their squares.
# Plot a scatter chart with:
#   * Blue points sized based on y-values
#   * A title: "Square Numbers Visualization"
#   * Axis labels and grid
#   * Use 'viridis' colormap
# Save the plot as 'squares_plot.png' using plt.savefig().

import matplotlib.pyplot as plt
# Generate data
x_values = list(range(1, 21))
y_values = [x**2 for x in x_values]
# Create scatter plot with colormap and size based on y-values
plt.scatter(x_values, y_values, c=y_values, cmap='viridis', s=[value * 10 for value in y_values])  # Scale point size by y-values
# Add labels, title, and grid
plt.xlabel("x values")
plt.ylabel("y values (squared)")
plt.title("Square Numbers Visualization")
plt.grid()
# Save the plot as 'squares_plot.png'
plt.savefig('squares_plot.png')
# Show the plot
plt.show()

