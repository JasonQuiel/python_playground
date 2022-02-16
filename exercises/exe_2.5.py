# fhand = open('mbox-short.txt')

#This does solve the file to upper case lab but I can reduce the code length
#for i in fhand:
#    i = i.rstrip()
#    i = i.upper() 
#    print(i)

#for i in fhand: 
#    i = i.rstrip()
#    print(i.upper())


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [11, 12, 13, 14, 15, 16, 17, 18]
c = a + b
print(c)

# two ways to make an empty list.
# mylist = []
# mylist = list()

mylist = list()

mylist.append(a)
mylist.append("freeCodeCamp")

print(mylist)

jumbled = [12, 3, 67, 4, 98, 35, 17, 44, 86, 53, 21, 56, 7, 11]

jumbled.sort()
print(jumbled)
print(sum(jumbled)) #adds all ints
print(max(jumbled)) #find max value

str = 'X-DSPAM-Confidence: 0.8475 '
word_list = str.split()
print(word_list) #splits into 'X-DSPAM-Confidence:', '0.8475'

another_piece = word_list[0].split('-') #splits the 1st index in the list at '-' leaving me with 'X', 'DSPAM', 'Confidence:
print(another_piece)