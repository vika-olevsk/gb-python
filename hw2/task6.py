items = []

i=1
while True:
    descr = input('Enter name, price, amount, unit. All separated by space:')
    if descr == 'stop':
        break
    descr = descr.split()
    items.append((i,{'name': descr[0], 'price': descr[1], 'amount': descr[2], 'unit': descr[3]}))
    i += 1


an_dict = {'names':[], 'prices':[], 'amount':[], 'units':[]}
for el in items:
    an_dict['names'].append(el[1]['name'])
    an_dict['prices'].append(el[1]['price'])
    an_dict['amount'].append(el[1]['amount'])
    an_dict['units'].append(el[1]['unit'])

print(an_dict)

