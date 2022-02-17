fhand = open('words.txt',)

count = 0

for line in fhand:
    count = count + 1
print('Our line count:', count)

# finding lines that start with 'from'

fcdc = open('mbox-short.txt')

for new in fcdc:
    new = new.rstrip() #rstrip removes the blank \n space between the lines of from - The print statement adds these blank lines.
    if new.startswith('From'):
        print(new)

# prints the days of the week using the position of a list using from as a start point.
days = open('mbox-short.txt')

for search in days:
    remove_n = search.rstrip() # removes the new line \n
    x = remove_n.split() #breakes the string into a list.
    if len(x) < 1:
        continue
    if x[0] != 'From':
        continue
    print(x[2])