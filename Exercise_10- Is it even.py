# Exercise 10- Is it even?
# Create a function to ask the user to input a number
def main():
    number = int(input("Enter a number: "))
    # Call even_or_odd and store the result
    result = even_or_odd(number)
    print(result) # print the result
# Create a function to determine if a number is even or odd
def even_or_odd(number):
    if number % 2 == 0:
        return(f"The number {number} is even.")
    else:
        return(f"The number {number} is odd.")
main()