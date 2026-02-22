# ==========================================
# Exercise 8: Loading Data with pandas
# ------------------------------------------
# Create a simple DataFrame using pandas:
#   data = {'Year': [2020, 2021, 2022, 2023], 'Sales': [150, 200, 250, 300]}
# Plot 'Year' on the x-axis and 'Sales' on the y-axis using plt.plot().
# Add appropriate labels and title.

import matplotlib.pyplot as plt
import pandas as pd
# Create a DataFrame
data = {'Year': [2020, 2021, 2022, 2023], 'Sales': [150, 200, 250, 300]}
df = pd.DataFrame(data)
# Plotting the data
plt.plot(df['Year'], df['Sales'], marker='o')
# Adding labels and title
plt.xlabel("Year")

plt.ylabel("Sales")
plt.title("Yearly Sales Growth")
# Show the plot
plt.show()

