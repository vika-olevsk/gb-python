from devices import Printer, Scanner, Xerox

class MyErr(Exception):
    def __init__(self, txt):
        self.txt = txt

class Storage:
    def __init__(self) -> None:
        self.storage_info = {'Store' : {'Printer': 10, 'Xerox': 10, 'Scanner': 10},
                             'Sales' : {'Printer': 0, 'Xerox': 0, 'Scanner': 0}, 
                             'Dev' : {'Printer': 0, 'Xerox': 0, 'Scanner': 0}, 
                             'Marketing' : {'Printer': 0, 'Xerox': 0, 'Scanner': 0}}
    def get_device(self, device, department, num):
        device = device.__class__.__name__
        try:
            if type(num) != int:
                raise MyErr('Can not recieve a device, num is not a number!')
            elif num > self.storage_info[str(department)][str(device)]:
                raise MyErr(f'Can not recieve a device, not enough devices in the {department} department!')
            self.storage_info['Store'][str(device)] += num
            self.storage_info[str(department)][str(device)] -= num
            print(f'Device {device} was recieved from {department} department')
        except MyErr as err:
            print(err)

    def give_device(self, device, department, num):
        device = device.__class__.__name__
        try:
            if type(num) != int:
                raise MyErr('Can not give a device, num is not a number!')
            elif num > self.storage_info['Store'][str(device)]:
                raise MyErr('Can not give a device, not enough devices in the store!')
            self.storage_info['Store'][str(device)] -= num
            self.storage_info[str(department)][str(device)] += num
            print(f'Device {device} was given to {department} department')
        except MyErr as err:
            print(err)




pr1 = Printer('test.txt', 10, True)
xr1 = Xerox('test.txt', 12, False, 2)
sc1 = Scanner('test.txt', 2)
pr1.to_print()
xr1.to_copy()
sc1.to_scan()

act = Storage()
act.give_device(xr1, 'Dev', 3)
act.give_device(sc1, 'Sales', 'dsds')
act.give_device(sc1, 'Sales', 2)
act.give_device(pr1, 'Dev', 5)
act.give_device(pr1, 'Sales', 6)
act.give_device(sc1, 'Marketing', 6)
act.get_device(pr1, 'Sales', 'lala')
print(act.storage_info)



