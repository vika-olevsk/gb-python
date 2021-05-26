from sys import argv
from itertools import count, cycle

# part a
print('Part a')
num = int(argv[1])
for el in count(num):
    print(el)
    if el == num + 5:
        break

# part b
print('Part b')
list = [1, 3, 5, 7]
с = 0
for el in cycle(list):
    if с == 6:
        break
    print(el)
    с += 1