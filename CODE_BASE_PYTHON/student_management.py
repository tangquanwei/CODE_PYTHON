# 学生的信息可以使用一个字典类型
# 管理学生可以使用列表
import os

# 定义全局变量学生列表
student_list = []  # list()
print("全局变量:", id(student_list))

# 显示功能菜单的函数


def show_menu():
    print("-----学生管理系统v1.0-----")
    print("1. 添加学生")
    print("2. 删除学生")
    print("3. 修改学生信息")
    print("4. 查询学生信息")
    print("5. 显示所有学生信息")
    print("6. 退出")


# 添加学生
def add_student():
    name = input("请输入学生的姓名:")
    age = input("请输入学生的年龄:")
    sex = input("请输入学生的性别:")

    # 定义学生字典类型的变量
    student_dict = {}  # dict()
    # 把学生的信息使用字典进行存储
    student_dict["name"] = name
    student_dict["age"] = age
    student_dict["sex"] = sex
    # 这里可以不使用global因为列表是可变类型，可以在原有数据的基础上进行修改，内存地址不变
    # 因为列表的内存地址不变，全局变量不需要使用global
    # 加上global表示内存地址要发生变化

    # 把学生信息添加到学生列表中
    student_list.append(student_dict)
    # global student_list
    # # student_list = [{'name': "李四", "age":"18", "sex":"男"}]
    # student_list.append(student_dict)


# 显示所有学生信息
def show_all_student():
    # print(student_list, id(student_list))
    for index, student_dict in enumerate(student_list):
        # 学号和下标的关系
        student_no = index + 1

        print("学号:%d 姓名:%s 年龄:%s 性别:%s" % (student_no, student_dict["name"],
                                           student_dict["age"], student_dict["sex"]))


# 删除学生信息
def remove_student():
    student_no = int(input("请输入要删除学生的学号:"))
    # 获取学生字典信息的下标
    index = student_no - 1
    if index >= 0 and index < len(student_list):
        # 根据下标删除学生信息
        del student_list[index]
    else:
        print("请输入正确的学号")

# 修改学生信息


def modify_student():
    student_no = int(input("请输入要修改学生的学号:"))
    # 根据学号计算下标
    index = student_no - 1

    if index >= 0 and index < len(student_list):
        # 根据下标获取学生字典信息
        student_dict = student_list[index]

        name = input("请输入您修改后的名字:")
        age = input("请输入您修改后的年龄:")
        sex = input("请输入您修改后的性别:")

        student_dict["name"] = name
        student_dict["age"] = age
        student_dict["sex"] = sex
    else:
        print("请输入正确的学号")


# 查询学生
def search_student():
    name = input("请输入要查询的学生姓名:")

    # 遍历学生列表信息
    for index, student_dict in enumerate(student_list):
        # pass # 空实现
        if student_dict["name"] == name:
            student_no = index + 1
            # 说明找到了这个学生
            print("学号:%d 姓名:%s 年龄:%s 性别:%s" % (student_no, student_dict["name"],
                                               student_dict["age"], student_dict["sex"]))
            break
    else:
        print("对不起，没有找到这个学生")


# 保存学生列表数据到文件中
def save_data():
    file = open("student_list.data", "w", encoding="utf-8")
    # 把列表转成字符串
    student_list_str = str(student_list)
    # 把列表数据写入到文件中
    file.write(student_list_str)
    file.close()


# 加载文件中的数据
def load_data():

    result = os.path.exists("Test")
    print(result)
    # 判断文件或者文件夹是否存在
    if os.path.exists("student_list.data"):
        file = open("student_list.data", "r", encoding="utf-8")

        # 读取文件中的数据
        file_content = file.read()
        new_student_list = eval(file_content)
        print(new_student_list, type(new_student_list))
        # global student_list
        # student_list = new_student_list

        student_list.extend(new_student_list)
        print("全局变量:", id(student_list))

        file.close()

# 程序启动的函数


def run():

    # 加载文件中的数据
    load_data()

    while True:
        # 显示功能菜单
        show_menu()
        # 接收用户的指令
        menu_option = input("请输入您需要的功能选项:")

        if menu_option == "1":
            print("添加学生")
            add_student()
        elif menu_option == "2":
            print("删除学生")
            remove_student()
        elif menu_option == "3":
            print("修改学生信息")
            modify_student()
        elif menu_option == "4":
            print("查询学生信息")
            search_student()
        elif menu_option == "5":
            print("显示所有学生信息")
            show_all_student()
        elif menu_option == "6":
            # 保存数据到文件
            save_data()
            print("退出")
            break


# 执行程序启动的函数
run()
