
#use find to find the number at the end of the str variable 0.8475 and slice it and turn it into a float.
str = 'X-DSPAM-Confidence: 0.8475 '

lower_case = str.lower() #this won't change all the letters to lower, it just makes a copy of the string in lower case.  So not needed for this.
print(lower_case)

target = len(str) #total length of the string

start = str.find('0') #returns the index of 20 for 0
print(start)

end = str.find(' ', start) #returns the blank space after 5 at index 26.  find the white space after the start variable
print(end)

goal = str[start : end]
print(goal)

our_number = float(goal)

print(type(our_number))