data = {}

with open('task6.txt', 'r') as f:
    for line in f:
        line = line.split()
        
        total_hours = 0
        for el in line:
            if '(' in el:
                ind = el.find('(')
                total_hours += int(el[:ind])

        lesson = line[0][:-1]
        data[lesson] = total_hours

print(data)