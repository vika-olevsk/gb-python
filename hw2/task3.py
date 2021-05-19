n = int(input('Enter the number of the month:'))

list_months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
print('From list: month is %s' % list_months[n-1])

dict_months = {1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 
                10:'Oct', 11:'Nov', 12:'Dec'}
print('From dict: month is %s' % dict_months.get(n))
