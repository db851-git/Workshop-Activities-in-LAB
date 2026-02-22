# ======================================
# 9. Tuples
# --------------------------------------
# Create a tuple called dimensions with two values (width, height).
# Print each value using a loop.
# Try changing one of the values (should cause an error) and note what happens.
# Reassign the tuple to a new pair of values and print it again.

# Creating a tuple called dimensions with two values (width, height)

dimensions = (1920, 1080)
# Printing each value using a loop
for dimension in dimensions:
    print(dimension)
# Trying to change one of the values (this will cause an error)
try:
    dimensions[0] = 1280  # This will raise a TypeError because tuples are immutable
except TypeError:
    print("Error: Tuples are immutable and cannot be changed after they are created.")
# Reassigning the tuple to a new pair of values and printing it again
dimensions = (1280, 720)
print("Updated dimensions:", dimensions)


        