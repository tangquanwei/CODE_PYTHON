class Person():
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = ['Error', gender][gender in ['Male', 'Female']]

    @property
    def personInfo(self):
        print("name:", self.__name, "\nage:",
              self.__age, "\ngender:", self.__gender)

    @property
    def getName(self):
        return self.__name

    @property
    def getAge(self):
        return self.__age

    @property
    def getGender(self):
        return self.__gender


class Score():
    subject = {'m': "高数", 'e': "英语", 'c': "C语言", 'g': "线性代数", 'f': "放风筝"}


class Student(Person,Score):
    def __init__(self, name, age, gender, collage, class_, **scores):
        super().__init__(name, age, gender)
        self.__collage = collage
        self.__class = class_
        self.__scores = scores

    @property
    def personInfo(self):
        print("name:", self.__name, "\nage:", self.getAge, "\ngender:",
              self.getGender, "\ncollage:", self.__collage, "\nclass:", self.__class)

    def study(self, teacher):
        print(f"{teacher.getName}老师,我终于学会了{teacher.teachObj}")

    def __str__(self):
        return "name:" + self.getName + "\nage:" + self.getAge + "\ngender:" + self.getGender + "\ncollage:" + self.__collage + "\nclass:" + self.__class

    __repr__ = __str__

    def getGPA(self):
        return sum([(eval(i[1:])/10-5)*j for i, j in self.__scores.items()])/sum([j for j in self.__scores.values()])

    def chScore(self, **scores):
        self.__scores = {i: j for i, j in self.__scores.items()
                         if i[0] != str(scores.keys())[12]}
        self.__scores.update(scores)
        return self

    @property
    def showScores(self):
        print("Your Scores are followed:")
        for i in self.__scores:
            print(Score.subject[i[0]], ':', i[1:])


class Teacher(Person):
    def __init__(self, name, age, gender, college, professional):
        super().__init__(name, age, gender)
        self.__collage = college
        self.__professional = professional

    @property
    def personInfo(self):
        print("name:", self.getName, "\nage:", self.getAge, "\ngender:", self.getGender,
              "\ncollage:", self.__collage, "\nprofessional:", self.__professional)

    @property
    def teachObj(self):
        return '今天讲的如何面向对象设计程序'


p1 = Person("Quanwei", "18", "Male",)
s1 = Student("Quanwei", "18", "Male", "电信学院", "软件2002",m80=6, e70=4, c90=4, g80=2, f100=10)
s2 = Student("Dog", "18", "Female", "电信学院", "软件2002")
s3 = Student("Wangcai", "18", "male", "电信学院", "软件2002")
t1 = Teacher("Zhou", "28", "Male", "电信学院", "Python")
# p1.personInfo
# t1.personInfo
# s1.study(t1)
# for i in [s1, s2, s3]:
#     print(i)
print("Your GPA is :", s1.getGPA())
s1.showScores
