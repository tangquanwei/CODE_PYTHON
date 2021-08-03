import math


class Circle(object):
    _radius = 0

    def __init__(self, r) -> None:
        self._radius = r

    def set_radius(self, r):
        self._radius = r

    def get_radius(self):
        return float(self._radius)

    def get_circumference(self):
        return 2*math.pi*self._radius

    def get_area(self):
        return math.pi*self._radius*self._radius

    def __del__(self):
        print(f'{self}对象已经被删除')


class SolidSphere(Circle):
    _radius = 0

    def get_circumference(self):
        return 2*math.pi*self._radius

    def get_area(self):
        return 4*math.pi*self._radius*self._radius

    def get_volume(self):
        return 4/3*math.pi*self._radius*self._radius*self._radius



