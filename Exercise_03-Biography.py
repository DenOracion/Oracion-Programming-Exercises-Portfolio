#Exercise 3 - Biography

#Ask user to input their name, age, hometown
name = input("Please enter your first name: ")
name2 = input("Please enter your second name:")
hometown = input("Please enter your hometown: ")
# Ask user for age, however it's only allowed to input a numerical value
try:
    age = int(input("Enter your age:"))
except ValueError:
    print("Please enter a number for your age")
# record the information given into a dictionary
Biography = {
    'First Name' : name,
    'Second Name' : name2,
    'Hometown' : hometown,
    'Age' : age
}
#print out the information in separate lines while maintaining one line of code using \n
print(f"Your  first name is: {Biography['First Name']} \nYour second name is: {Biography['Second Name']} \nYour hometown is: {Biography['Hometown']} \nYour age is: {Biography['Age']}")


