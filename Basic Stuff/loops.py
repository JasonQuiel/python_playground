
# A while loop example to count down pizza slices.

pizza = 12

while pizza >= 0:
    print("The remaining slices are: ", pizza)
    pizza -= 1


while True:
    magic_word = input("Say Please to stop the loop ")
    if magic_word == "Please":
        break
    print(magic_word.capitalize())

