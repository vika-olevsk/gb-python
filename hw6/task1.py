import time

class TrafficLight:
    __color = 'red' ## class variable,
    
    def running(self):
        times = 0
        while times < 5:
            print(f'{TrafficLight.__color} color!')
            if TrafficLight.__color == 'red':
                time.sleep(7)
                TrafficLight.__color = 'yellow'
            elif TrafficLight.__color == 'yellow':
                time.sleep(2)
                TrafficLight.__color = 'green'
            elif TrafficLight.__color == 'green':
                time.sleep(5)
                TrafficLight.__color = 'red'
            times +=1


tl1 = TrafficLight()
tl1.running()