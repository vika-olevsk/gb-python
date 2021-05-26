from sys import argv

hours, payout, bonus = map(int, argv[1:])
print('Salary is %i' % (hours * payout + bonus))