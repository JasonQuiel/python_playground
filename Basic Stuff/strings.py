# Working with strings!

home_state = 'Minnesota' 
x = len(home_state)
#print(x) # lenght of the string

letter = home_state[8]
#print(letter) # the letter of the index of 8

m = 5
minus = home_state[m - 4] 
#print(minus)


for count in home_state:
    print(count)

buzz_word = "Mississippi"
sum_of_s = 0

for hold in buzz_word:
    if hold == 's':
        sum_of_s = sum_of_s + 1

print(sum_of_s) # total number of s in mississippi

paragraph = " is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters,/ as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like)."
v = len(paragraph)
print(v)
total_a = 0

for i in paragraph:
    if i == 'a':
        total_a = total_a + 1

print(total_a)

buzz_word = "Mississippi"
's' in buzz_word

buzz_word = "MISSISSIPPI"
stop_yelling = buzz_word.lower()
print(stop_yelling)

print('HELLO FROM THE OTHER SIDE'.lower())

buzz_word = "mississippi"
speak_up = buzz_word.upper()
print(speak_up)

buzz_word = "Mississippi"
state_change = buzz_word.replace('Mississippi', 'Minnesota')
print(state_change)

buzz_word = "Mississippi"
letter_change = buzz_word.replace('s', 'x')
print(letter_change)


