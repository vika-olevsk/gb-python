import json

data = {}

with open('task7.txt', 'r') as f:
    total_profit = 0
    for i, line in enumerate(f):
        line = line.split()

        revenue = int(line[2])
        costs = int(line[3])
        profit = revenue - costs

        if profit > 0:
            total_profit += profit

        name = line[0]
        data[name] = profit
    data['avg_profit'] = total_profit/i

print([data])

with open("task7.json", "w") as json_f:
    json.dump(data, json_f)