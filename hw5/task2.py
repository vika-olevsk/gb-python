with open("task2.txt") as f:
    for i, line in enumerate(f):
        n = line.split()
        print('Line %d contains %d words' % (i+1,len(n)))
    print('File has %d lines' % (i+1))