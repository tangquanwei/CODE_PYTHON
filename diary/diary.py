def add():

    global diary_ls  # ! 不声明下一句不能添加  why?  如果局部要对全局变量*修改*，则在局部声明该全局变量
    diary_ls.extend(['date:'+input(' ˙ω˙ 今天是几月几号?(eg.6/8): '),
                    'wheather:'+input('今天天气怎么样: '),
                    'mood:'+input('今天心情怎么样: '),
                    'theme:'+input('日记的主题是: ')])
    print('好,现在开始愉快地写日记吧!')
    diary_ls.extend(sub_add())


def save():
    with open('./diary.txt', 'w', encoding='utf-8') as d:
        d.write('\n'.join(diary_ls))


def search():
    while True:
        try:
            (choice := int(input('请输入索引:\n1. 日期  2. 主题: '))) in [1, 2]
            break
        except ValueError:
            print("请你输入一个数字: 1 或 2")
            continue
    if not choice-1:
        s = input('请输入日期: ')
        index = 0
        for i in range(len(diary_ls)):
            if diary_ls[i] == 'date:'+s:
                index = i
                break
        else:
            print('没有找到!')
            return -1
        i = index
        while diary_ls[index].strip() != 'end_of_diary':  #! IndexError: 'end_of_diary\n'
            print(diary_ls[index])
            index += 1
        return i
    else:
        s = input('请输入主题: ')  # ***
        index = 0
        for i in range(len(diary_ls)):
            if diary_ls[i] == 'theme:'+s:  # ***
                index = i
                break
        else:
            print('没有找到!')
            return -1
        i = (index := index-3)  # ***
        while diary_ls[index].strip() != 'end_of_diary':  # IndexError: 'end_of_diary\n'
            print(diary_ls[index])
            index += 1
        return i  # date


def remove(index=-2):
    if index != -2 or (index := search()) != -1:
        while diary_ls[index] != 'end_of_diary':
            del diary_ls[index]
        del diary_ls[index]
    print(diary_ls)


def modify():
    if (index := search()) != -1:
        remove(index+4)
        global diary_ls
        diary_ls=diary_ls[:index+4]+sub_add()+diary_ls[index+4:]

def sub_add():
    middle=[]
    cnt=0
    while diary:=input(':'):
        middle.append(str(cnt)+' '+diary)
        cnt+=1
    middle.append('end_of_diary')
    return middle



def load():
    try:
        d = open('./diary.txt', 'r', encoding='utf-8')
    except FileNotFoundError:
        open('./diary.txt', 'w').close()
        d = open('./diary.txt', 'r', encoding='utf-8')
    finally:
        global diary_ls  # !必要
        diary_ls = d.read().strip().split('\n')
        d.close()
        print(diary_ls)


def show_all():
    for i in diary_ls:
        print([i, ''][i == 'end_of_diary'])


def main():
    load()

    while True:
        print("我的日记系统v8.3".center(20, '-') +
              "\n1. 添加日记     \
            \n2. 删除日记      \
            \n3. 修改日记信息   \
            \n4. 查询日记信息   \
            \n5. 显示所有日记信息\
            \n6. 退出")
        try:
            if (menu_option := int(input("请输入您需要的功能选项:"))-1) == 5:  #! ValueError
                save()
                print("退出")
                break
        except ValueError:
            print("请你输入一个数字")
            continue

        func_ls = [add, remove, modify, search, lambda:print(
            '\n'.join([[i, '\n'][i == 'end_of_diary'] for i in diary_ls]))]
        func_ls[menu_option]()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        ...
    # except IndexError:
    finally:
        print('谢谢使用 :)')


# todo Singleton
