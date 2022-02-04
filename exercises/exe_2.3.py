# A for loop to retrieve the largest number
start_number = 0

for random_numbers in [3, 4,67, 34, 12, 9, 89, 12, 55, 96, 1, 103]:
    if random_numbers > start_number:
        start_number = random_numbers
        #print(random_numbers) prints out the list 3, 4, 67, 89, 96, 103

print(random_numbers)

def small_number():
    number_holder = None

    for i in [132,765, 125, 987, 183,53, 78, 25, 122, 7]:
        if number_holder is None: #is key word is every powerful, so it makes sure None = None which is true.
            number_holder = i #so the first values is used which is 132.
            #print(number_holder) #number 132
        elif i < number_holder:
            number_holder = i
            print(number_holder)
small_number()

# just print off the list of numbers
for x in [3, 2, 1, 0]:
    print(x)
