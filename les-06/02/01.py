# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу:
# длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т

class Road:
    _length: int
    _width: int
    weight: int
    thickness: int

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self):
        self.weight = 25
        self.thickness = 5
        asphalt_mass = self._length*self._width*self.weight*self.thickness/1000
        print(f"Масса асфальта в тоннах — {asphalt_mass}")


road1 = Road(20, 5000)

road1.mass()
