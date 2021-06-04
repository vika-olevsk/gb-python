class Stationary:
    def __init__(self, t):
        self.title = t
    
    def draw(self):
        print('Start drawing!')

class Pen(Stationary):
    def draw(self):
        print(f'Start drawing with pen {self.title}!')

class Pencil(Stationary):
    def draw(self):
        print(f'Start drawing with pencil {self.title}!')

class Handle(Stationary):
    def draw(self):
        print(f'Start drawing with handle {self.title}!')


pen = Pen('rolex')
pen.draw()

pencil = Pencil('big')
pencil.draw()

handle = Handle('Red Guy')
handle.draw()