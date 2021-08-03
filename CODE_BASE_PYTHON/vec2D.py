import math


class Vec2D(object):
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def __del__(self):
        del self.__x
        del self.__y

    def __iadd__(self, vec2d):
        self.__x += vec2d.getX()
        self.__y += vec2d.getY()
        return self

    def __add__(self,vec2d):
        vec2d_temp=self
        return vec2d_temp.__iadd__(vec2d)

    def __isub__(self, vec2d):
        self.__x -= vec2d.getX()
        self.__y -= vec2d.getY()
        return self

    def __imul__(self, vec2d):
        return self.__x*vec2d.getx()+self.__y*vec2d.getY()

    def __mul__(self,vec2d):
        self.__mul__(vec2d)

    @property
    def norm(self):
        """ 返回向量的范数 """
        return math.sqrt(self.__x**2+self.__y**2)

    def __str__(self):  # 字符串打印
        return f"({self.__x}, {self.__y})"

    def __getitem__(self, pos):
        """ 按下标取值 """
        return [self.__x, self.__y][pos]

    def __ne__(self, vec2d):
        return self.norm != vec2d.norm

    def __eq__(self,vec2d):
        return self.__x==vec2d.getX() and self.__y==vec2d.getY()

    

    __repr__ = __str__  # 解释器打印


v1 = Vec2D(1, 2)
v2 = Vec2D(4, 3)
v3 = Vec2D(3, 4)
# print(v2.norm)
# print(v2[1])
# v3 == v2
v1+v2

def sayhi():
    print("HI Quanwei")

v1.sayhi=sayhi
v1.sayhi()

