from functools import reduce

list = [i for i in range(100, 1001) if i % 2 ==0]

def mult(fr,sec):
    return fr*sec

print(reduce(mult,list))