words = input('Enter lower case word:').split()

def int_func(word):
    asc = ord(word[0])
    word = chr(asc-32) + word[1:]
    return word

upper_case = [int_func(el) for el in words]
print(' '.join(upper_case))
