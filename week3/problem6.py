# ==========================================
# Exercise 6: Using a Colormap
# ------------------------------------------
# Create a scatter plot with 50 points where x = range(1, 51)
# and y = [value**2 for value in x].
# Use the 'plasma' colormap and scale point colors to y.
# Add a colorbar and label it.

import matplotlib.pyplot as plt
# Generate data
x = range(1, 51)
y = [value**2 for value in x]
# Create scatter plot with colormap
plt.scatter(x, y, c=y, cmap='plasma')
# Add colorbar and label
plt.colorbar(label='y values (squared)')
# Add labels and title
plt.xlabel("x values")
plt.ylabel("y values (squared)")
plt.title("Scatter Plot with Plasma Colormap")
# Show the plot
plt.show()
    