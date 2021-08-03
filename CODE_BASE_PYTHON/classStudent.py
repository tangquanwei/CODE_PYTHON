import functools
import time
import pysnooper


class Student(object):
    def __init__(self, name="unknown", gender='Male', stu_num="20203206000", **scores):
        self.__name = name
        self.__stu_num = stu_num
        self.__scores = scores
        if gender in ['Male', 'Female']:
            self.__gender = gender
        else:
            print("Gender Error")

    def getGender(self):
        return self.__gender

    def setGender(self, gender):
        self.__gender = gender
        return gender

    def log(text="Execute"):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print(f'{time.ctime()} {text} {func.__name__}():')
                return func(*args, **kw)
            return wrapper
        return decorator

    @log()
    def getGPA(self):
        points = 0
        total = 0
        for i, j in self.__scores.items():
            total += (eval(i[1:])/10-5)*j
            points += j
        return total/points

    @log()
    def getGPA_v2(self):
        return sum([(eval(i[1:])/10-5)*j for i, j in self.__scores.items()])/sum([j for j in self.__scores.values()])

    def chName(self, name):
        self.__name = name
        return self

    @log()
    def chScore(self, **scores):
        self.__scores = {i: j for i, j in self.__scores.items()
                         if i[0] != str(scores.keys())[12]}
        # for i in self.__scores.keys():
        #     for j in scores.keys():
        #         if i[0]==j[0]:
        #             del self.__scores[i]
        # 字典在遍历时不能进行修改，建议转成列表或集合处理。
        self.__scores.update(scores)
        return self

    @property
    def showInfo(self):
        print("Your name is: "+self.__name+"\nYour gender is: "+self.__gender+"\nStudent number is: " +
              self.__stu_num+"\nAnd your scores followed:")
        for i in self.__scores:
            print(subject[i[0]], ':', i[1:])

    def __str__(self):
        return f'Student object (name: {self.__name})'
    __repr__ = __str__


class Stu(object):
    @property
    def showInfo(self):
        print("My name is: Stu")


class Dent(object):
    @property
    def showInfo(self):
        print("My name is: Dent")


class Solution(Stu, Dent, Student):
    showInfo1 = Student.showInfo  # assign the name -> cp the func

    @property
    def showInfo(self):
        self.showInfo1


subject = {'m': "高数", 'e': "英语", 'c': "C语言", 'g': "线性代数", 'f': "放风筝"}
# ?                     课程简写 分数=学分
s1 = Student("Quanwei", m80=6, e70=4, c90=4, g80=2, f100=10)
s2 = Solution("Quanwei", m80=6, e70=4, c90=4, g80=2, f100=10)
print(s2.getGPA())
print(s2.getGPA_v2())
s2.chScore(m50=4).showInfo
# print(s1._Student__name)
# print(Solution("quanwei"))
# print('isinstance(s2, Student):',isinstance(s2, Student))
# print("isinstance(s2, Solution):",isinstance(s2, Solution))
# print("issubclass(Solution, Student):",issubclass(Solution, Student))
print("方法搜索顺序:", Solution.__mro__)
