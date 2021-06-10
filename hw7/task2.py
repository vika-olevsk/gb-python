from abc import ABC, abstractmethod

class Clothes:
    def __init__(self, name):
        self.name = name

    @property
    @abstractmethod
    def cloth_calc(self):
        pass

class Coat(Clothes):
    def __init__(self, name, V):
        super().__init__(name)
        self.V = V
    
    @property
    def cloth_calc(self):
        return self.V/0.65 +0.5 

class Suit(Clothes):
    def __init__(self, name, H):
        super().__init__(name)
        self.H = H
    
    @property
    def cloth_calc(self):
        return 2*self.H + 0.3 

item1 = Coat('HM', 5)
item2 = Suit('Tommy Hilfiger', 7)

print(item1.cloth_calc)
print(item2.cloth_calc)
