# ==========================================
# Exercise 3: Line Plot
# ------------------------------------------
# Create a list of x-values [1, 2, 3, 4, 5] and y-values [2, 4, 6, 8, 10].
# Use plt.plot() to plot x vs y.
# Add a title, and labels for x and y axes.
# Show the plot using plt.show().


from py_compile import main

import matplotlib.pyplot as plt
import pandas as pd
x_values = [1, 2, 3, 4, 5]
y_values = [2, 4, 6, 8, 10]
plt.plot(x_values, y_values)
plt.title("Line Plot of x vs y")
plt.xlabel("x values")
plt.ylabel("y values")
plt.show()

try:
    main()
except KeyboardInterrupt:
    pass  # or print a short message
