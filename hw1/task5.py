rev = int(input('Enter your revenue:'))
sp = int(input('Enter your spendings:'))

if rev > sp:
    print('Congrats! You have profit of %d' % (rev/sp))
    emp = int(input('Enter number of employees:'))
    print('Profit per employee is %d' % (rev/sp/emp))
else:
    print('Sorry, you have loss :(')


