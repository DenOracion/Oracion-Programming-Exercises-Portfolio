# First, create a dictionary where the keys are month numbers and the values are numbers of days in that month
days = {
    1 : 31,
    2 : 28,
    3 : 31,
    4 : 30,
    5 : 31,
    6 : 30, 
    7 : 31,
    8 : 31,
    9 : 30,
    10 : 31,
    11 : 30,
    12 : 31
}
# User will be asked to input the month number
month = int(input("Enter the month number (1-12):"))

# Validate month number
if month in days:
    # Unique case if February is holding a leap day
    if month == 2:
        leap_year = input("Is it a leap year? (Yes? or No?):")
        leap_year = leap_year.lower()
        if leap_year == "yes":
            print("February this year has 29 days. It is a leap year")
        else:
            print("February this year has 28 days")
    else:
        print(f"This month has {days[month]} days.")
else:
    print("The month number is invalid, Please try inputting a number between 1 and 12")