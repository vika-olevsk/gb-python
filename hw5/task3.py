with open("task3.txt") as f:
    summ = 0
    for i, line in enumerate(f):
        n = line.split()
        summ += int(n[1])
        if int(n[1]) < 20000:
            print(n[0] + ' has less than 20000')
    print('Average salary is %d' % (summ/i))