def sums(*args):
    a = list(args)[0]
    a = [int(el) for el in a]
    return sum(a)

res = 0
while True:
    input_list = input('Enter several numbers separated by space:').split()
    if '!' in input_list and len(input_list) == 1:
        break
    elif '!' in input_list:
        i = input_list.index('!')
        res += sums(input_list[:-i-1])
        print(f'Sum is {res}')
        break
    res += sums(input_list)
    print(f'Sum is {res}')
