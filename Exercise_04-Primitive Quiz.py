#Exercise 4 - Primitive Quiz

#Create a list of tuples containing European countries and their capitals
capitals = [
    ("France", "Paris"),
    ("Germany", "Berlin"),
    ("Spain", "Madrid"),
    ("Hungary", "Budapest"),
    ("Italy", "Rome"),
    ("Finland", "Helsinki"),
    ("Belgium", "Brussels"),
    ("Greece", "Athens"),
    ("United Kingdom", "London"),
    ("Poland", "Warsaw"),
]

#Loop through the tuples in the list 
for country, capital in capitals:
    answer = input(f"What is the capital of {country}?").strip().lower()
    if answer == capital.lower():
        print("You are correct!")
    else:
        print(f"You are incorrect! The capital of {country} is {capital}.")