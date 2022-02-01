#The standard Helloworld.

# Standard variables 

player_name = "Billy"
player_health = 100
game_is_over = bool

#Assign values to multiple names
one = uno = 1

print(uno)
print(one)

# A function is started with the def key word.

def main():
    name = input("What is your name? ")
    print("Nice to meet you,", name)
    print("Hello World")

main()

def elavator():
    upf = input("What floor do you need? ")
    # int() can change a string with numeric characters into a int.
    usf = int(upf) + 1  
    print("This is the USA floor you need!", usf)

elavator()

#Built in keyword type if you want to find out what something - type(thing)
a = 7
b = "string"
c = 7.8

print(type(a))
print(type(b))
print(type(c))

# Mathmatical Operators  +, -, *, (deciaml with remainder, / or rounded //) 
# % between two number will return the remainder and ** lets you mix ints with floats
# 
# Order of Operations in python
# Parenthesis, Power, Multiplication, addition, left to right  