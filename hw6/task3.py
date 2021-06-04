class Worker:
    def __init__(self, n, surn, pos, inc):
        self.name = n
        self.surname = surn
        self.position = pos
        self._income = inc
        

class Position(Worker):
    def get_full_name(self):
        print(f'Full name is {self.name} {self.surname}')
    def get_total_income(self):
        print('Total income is %d' % (self._income['wage']+ self._income['bonus']))


pos1 = Position('Vika', 'Olevsk', 'Ps En', {'wage': 1000, 'bonus': 500})
pos1.get_full_name()
pos1.get_total_income()

pos2 = Position('Ser', 'Val', 'Biz An', {'wage': 2000, 'bonus': 900})
pos2.get_full_name()
pos2.get_total_income()