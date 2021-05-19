line = input('Enter couple of words:')

line = line.split()
for i, el in enumerate(line):
    print(i+1, el[0:10])