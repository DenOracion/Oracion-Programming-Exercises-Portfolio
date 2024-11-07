# Exercise 8 - Simple Search

# First create a list containing the names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
# Ask the user to input the name to find
search = input("Enter the name you want to find:")
# Check if the name the user is searching for is in the list
if search in names:
    print(f'{search} was found in the list.')
else:
    print(f'{search} was not found in the list.')