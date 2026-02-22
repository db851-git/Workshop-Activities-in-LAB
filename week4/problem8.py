# ==========================================
# Exercise 8: Looping Through a Dictionary
# ------------------------------------------
# Create a dictionary of favorite_languages:
#   favorite_languages = {'Alice': 'Python', 'Bob': 'C', 'Charlie': 'JavaScript'}
# Loop through the dictionary and print:
#   "Alice's favorite language is Python."

# Create a dictionary of favorite_languages
favorite_languages = {
    'Alice': 'Python',
    'Bob': 'C',
    'Charlie': 'JavaScript'
}
# Loop through the dictionary and print each person's favorite language
for name, language in favorite_languages.items():
    print(f"{name}'s favorite language is {language}.")
        