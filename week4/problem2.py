# ==========================================
# Exercise 2: if-elif-else Chains
# ------------------------------------------
# Create a variable temperature = 25
# Write an if-elif-else chain that:
#   * prints "It's cold!" if temperature < 10
#   * prints "It's mild." if temperature is between 10 and 25
#   * prints "It's hot!" if temperature > 25

# Create a variable temperature
temperature = 25
# Write an if-elif-else chain to check the temperature
if temperature < 10:
    print("It's cold!")
elif 10 <= temperature <= 25:
    print("It's mild.")
else:
    print("It's hot!")

        