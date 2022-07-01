# creating a while loop that uses break and continue.

while True:
    int_value = input("Put in a number and remember to say Please to stop the loop: ")
    if int_value == "Please":
        break
    number = int(int_value)
    if number % 2 == 0:
        continue
print(number, "The square is: ", number * number)


# Another while loop,

number_sequ = [1, 3, 5, 7, 9, 11]
# Start checking at index 0 in the list
position = 0
# While the position is less than the lenght of the list, keep checking
while position < len(number_sequ):
# number_check holds the values to compaire as it goes through the list
    number_check = number_sequ[position]
    if number_check % 2 == 0:
        print("Found an even number!", number_check)
        break
    position += 1 # Moves the index up by 1 for each loop until the end.
else:
    print("No even number was found")


#guess me

magic_number = 8
guess = 1

while True:
    if guess < magic_number:
        print("To low")
    elif guess == magic_number:
        print("Spot on!")
        break
    elif guess > magic_number:
        print("oops")
    guess += 1


