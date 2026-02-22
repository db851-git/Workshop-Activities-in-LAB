# ==========================================
# Exercise 7: Using get() Safely
# ------------------------------------------
# Try to access a key called 'country' using person.get('country', 'Not specified').
# Print the result.

# Create a dictionary called person
person = {
    'name': 'Alice',
    'age': 25,
    'city': 'London',
    'country': 'UK'
}
# Try to access a key called 'country' using get()
country = person.get('country', 'Not specified')
# Print the result
print(country)

