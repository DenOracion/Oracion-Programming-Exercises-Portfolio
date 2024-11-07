# Exercise 7 - Some Counting

# We will create several loops in this exercise

# Loop 1 - Write a loop that counts up from 0 to 50 in increments of 1
print("0 to 50:") 
for x in range(0, 51):
    print(x) # when the program is executed, the code will print out numbers from 0 to 50 in steps of 1

# Loop 2 - Write a loop that counts down from 0 to 50 in decrements of 1
print ("50 to 0:")
for x in range(50, 1, -1):
    print(x) # this time the line of code will print out numbers from 0 to 50, steps of 1

# Loop 3 - Write a loop that counts up from 30 to 50 in increments of 1
print("30 to 50:")
for x in range(30, 51):
    print(x) # the line of code will start from 30 and count up to 50 in steps of 1

# Loop 4 - Write a loop that counts down from 50 to 10 in decrements of 2
print("50 to 10 in decrements of 2:")
for x in range(50, 9, -2):
    print(x) # this time the code will countdown from 50 to 10 steps of 2

# Loop 5 - Write a loop that counts up from 100 to 200 in increments of 5
print("100 to 200 in increments of 5:")
for x in range(100, 201, 5):
    print(x) # the line of code will count from 100 to 200 in steps of 5