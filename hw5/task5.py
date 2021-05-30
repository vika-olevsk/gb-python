import random

with open('task5.txt', 'w+') as f:
    nums = ' '.join([str(i + random.randint(0, 10)) for i in range(10)])
    f.write(nums)

    f.seek(0)
    sum_nums_in_file = sum(list(
                            map(int, f.read().split())
                            ))
    print(sum_nums_in_file)
