rus_nums = {1: 'Один', 2: 'Два', 3: 'Три', 4: 'Четыре'}

with open('task4.txt', 'r') as f_en, open('task4_ru.txt', 'w') as f_ru:
    for line in f_en:
        print(rus_nums.get(int(line[-2])) + line[-5:])
        f_ru.write(rus_nums.get(int(line[-2])) + line[-5:])
