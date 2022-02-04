
add = 0
total = 0

while True:
    number_input = input("Enter a number: ")
    if number_input == 'done':
        break
    try:
        value = float(number_input)
    except:
        print("Not a valid number")
        continue

    total = total + value
    add = add + 1

print(total, add, total/add)