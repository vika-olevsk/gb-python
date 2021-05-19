list = []
while True:
    el = input('Enter element:')
    if el == 'stop':
        break
    list.append(el)
print(list)

new_list = []
i=0
while i < len(list):
    if i == (len(list)-1):
        new_list.append(list[i])
        break
    new_list.append(list[i+1])
    new_list.append(list[i])
    i += 2

print(new_list)
