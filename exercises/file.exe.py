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

