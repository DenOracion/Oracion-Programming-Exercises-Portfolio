# Exercise 6 - Brute Force Attack

# First define the correct password
password = '12345'
maximum_attempts = 5 # Limit to how many incorrect attempts are allowed
attempts = 0 # attempt counter
# Use a while loop to allow multiple attempts
while attempts < maximum_attempts:
    enter_password = input("Please enter the password:") # asks the user to input a password
    attempts += 1 # increase the password attempt counter
    # Check if the entered password is correct
    if enter_password == password:
        print("Access Granted")
    else:
        remaining_attempts = maximum_attempts - attempts # calculates remaining attempts
        if remaining_attempts > 0:
            print(f"Incorrect password! You have {remaining_attempts} attempts remaining") 
        else:
            print("You have used up all the attempts, The authorities have been alerted.") # when all 5 attempts have been used, a message notifying the user the authorities have been alerted will be printed


