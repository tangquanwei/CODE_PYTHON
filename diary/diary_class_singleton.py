def singleton(cls):
    _instance = {}

    def inner():
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]
    return inner


@singleton
class Diary(object):
    __diary_ls = []

    def __init__(self):
        # * 主程序入口
        try:
            self.__main()
        except KeyboardInterrupt:
            ...
        finally:
            print('谢谢使用 :)')

    def add(self):
        Diary.__diary_ls.append('date:'+input(' ˙ω˙ 今天是几月几号?(eg.6/8): ')+'\n' +
                                'wheather:'+input('今天天气怎么样: ')+'\n' +
                                'mood:'+input('今天心情怎么样: ')+'\n' +
                                'theme:'+input('日记的主题是: '))
        print('好,现在开始愉快地写日记吧!')
        cnt = 0
        while diary := input('>'):
            Diary.__diary_ls.append(str(cnt)+' '+diary)
            cnt += 1
        Diary.__diary_ls.append('end_of_diary\n')

    def save(self):
        with open('./diary.txt', 'w', encoding='utf-8') as d:
            d.write('\n'.join(Diary.__diary_ls))

    def search(self):
        s = input('请输入日期: ')
        index = 0
        for i in range(len(Diary.__diary_ls)):
            if (ls := Diary.__diary_ls[i]) == (aim := 'date:'+s):
                index = i
                break
        else:
            print('没有找到!')
            return -1
        i = index
        while Diary.__diary_ls[index] != 'end_of_diary':
            print(Diary.__diary_ls[index])
            index += 1
        return i

    def remove(self, index=-2):
        if index != -2 or (index := self.search()) != -1:
            while Diary.__diary_ls[index] != 'end_of_diary':
                del Diary.__diary_ls[index]
            del Diary.__diary_ls[index]

    def modify(self):
        if (index := self.search()) != -1:
            self.remove(index)
            self.add()

    def load(self):
        with open('./diary.txt', 'r', encoding='utf-8') as d:
            Diary.__diary_ls = d.read().strip().split('\n')
            print(Diary.__diary_ls)

    def __main(self):
        self.load()

        while True:
            print("我的日记系统v3.0".center(20, '-') +
                  "\n1. 添加日记     \
                \n2. 删除日记      \
                \n3. 修改日记信息   \
                \n4. 查询日记信息   \
                \n5. 显示所有日记信息\
                \n6. 退出")
            try:
                if (menu_option := int(input("请输入您需要的功能选项:"))-1) == 5:
                    self.save()
                    print("退出")
                    break
            except ValueError:
                print("请你输入一个数字")
                continue

            func_ls = [self.add,
                       self.remove,
                       self.modify,
                       self.search,
                       lambda:
                       print('\n'.join([[i, ''][i == 'end_of_diary']
                                        for i in Diary.__diary_ls]))
                       ]
            func_ls[menu_option]()


Diary1 = Diary()
# print(__diary_ls)
