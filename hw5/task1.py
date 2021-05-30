f = open("task1.txt", "w")

while True:
    text = input('Enter something:')
    print(text)
    if text == '':
        break
    f.write(text+'\n')
    
f.close()