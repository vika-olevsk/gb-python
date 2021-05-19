input_secs = int(input('Enter time in secs:'))

hours = input_secs // 3600
mins = input_secs % 3600 // 60
secs = input_secs % 3600 % 60

print('Time is %02d:%02d:%02d' % (hours,mins,secs))