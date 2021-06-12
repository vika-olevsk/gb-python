class MyErr(Exception):
    def __init__(self, txt):
        self.txt = txt


final_list = []
while True:
    el = input('Enter a number:')
    if el == 'stop':
        break
    try:
        if not el.isnumeric():
            raise MyErr('Not a number!!')
        el = int(el)
        final_list.append(el)
    except MyErr as err:
        print(err)
    
print(final_list)