class Road:
    mass_alsph_per_cm = 25
    cms = 5

    def __init__(self,l, w):
        Road._lengh = l
        Road._width = w

    def calc_asph_mass(self):
        return self._lengh * self._width * Road.mass_alsph_per_cm * Road.cms


rd1 = Road(2,3)
print(rd1.calc_asph_mass())

rd2 = Road(20,30)
print(rd2.calc_asph_mass())