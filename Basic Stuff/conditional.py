# comparison operators
# < less than, > greater than, <= less than or equal to, >= greater than or equal to
# == equal to, != not equal to


# If else statement

first_player = "John"

if first_player != "Bob":
    print('Hello New Player')
else:
    print("Welcome back Bob")


# Function with if and elif conditions

def movement(x_pos, y_pos):
    if x_pos < y_pos:
        print("You move 1 space")
    elif x_pos > y_pos:
        print("You move 2 spaces")
    elif x_pos == y_pos:
        print('Lose a turn!')
movement(8, 9)

# try and execpt 

user_number = input("Enter a number: ")
try:  # Try to convert the string to an int but you can don't throw a traceback just move to except
    invalid = int(user_number)
except:
    invalid = -1


if invalid > 0: # So if anything that has been converted greater than 0 will print "Nice Job"
    print("Nice Job")
else:
    print("Not a valid number")
