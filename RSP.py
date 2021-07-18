""" 实现比较的的核心函数 """
def Play_v1(your_choice):         #传入用户的选择
    global c                   # 声明成全局变量共其他函数使用
    c=random.randint(0,2) 
    if dct[your_choice]==0 :   # 判断用户输入的内容
        if c==0:               # 判断内置选择的类容
            return 0           # 返回值代表的3种含义
        elif c==1:             # 0 draw,1 win,-1,lose
            return 1
        elif c==2:             # 这里也可以直接else
            return -1
    elif dct[your_choice]==1:
        if c==0:
            return -1          # 0 draw,1 win,-1,lose
        elif c==1:
            return 0
        elif c==2:
            return 1
    elif dct[your_choice]==2:
        if c==0:
            return 1           # 0 draw,1 win,-1,lose
        elif c==1:
            return -1
        elif c==2:
            return 0


""" 实现游戏过程的核心函数 """
def Begin():
    YoN=input("你要用钱玩游戏么？(y/n):")                               # 是否算钱
    if YoN=='y' or YoN=='yes':                                              # 输入其他的就不管了
        opin=True
        global money
        money=int(input("那你打算花多少钱呢？"))
    else:
        opin=False
    while True:
        your_choice=input("Plese,Enter\n石头\t剪刀\t布\nR\tS\tP\nr\ts\tp\n") # 提示用户输入
        while your_choice not in dct:
            your_choice=input("Error!\nEnter（石头、剪刀、布）:")            # 循环，直到输入正确，ctrl+c结束
        ret_val=Play_v1(your_choice)
        if ret_val==-1:                                                     # 根据返回值判断输赢
            print(f"Your'{your_choice}',my'{dit[c]}'.You lose :(")
        elif ret_val==0:
            print(f"Your'{your_choice}',my'{dit[c]}'.We draw :|")
        elif ret_val==1:
            print(f"Your'{your_choice}',my'{dit[c]}'.You win :)")
        if opin:
            Money(ret_val)
            if money:
                print(f"You have ￥{money}.")
            else:
                print("You Over!")
        YoN=input("Again? key in no/n to quit:")                            # 让用户确定是否还玩儿
        if YoN=='no' or YoN=='n':
            break

""" 用来算钱的函数 """
def Money(judge):
    global money                 # 用全局变量带出money值
    if judge==-1:
        money-=50
    elif judge==1:
        money+=50

import random

""" 简化比较的核心函数 """
def Play_2(your_choice):        # 传入用户输入的出拳选择
    choice_ls = ["剪刀", "石头", "布"]      # 可能的选择
    win_ls = [["石头", "剪刀"], ["剪刀", "布"], ["布", "石头"]]
    macs_choice = random.choice(choice_ls)      #从list里面选择一个
    print(f"your choice is {your_choice},Mac's choice is {macs_choice}")
    if your_choice in choice_ls:        # 判断输入是否正确
        print(f"your choice is {your_choice},Mac's choice is {macs_choice}")
        if your_choice == macs_choice:      # 平局
            return 0
        elif [your_choice, macs_choice] in win_ls:      # 赢了
            return 1
        else:       #输了
            return -1
    else:
        print("Input Error!")


""" 去掉平局 """
def Play_3(your_choice):
    choice_ls = ["剪刀", "石头", "布"]
    win_ls = [["石头", "剪刀"], ["剪刀", "布"], ["布", "石头"]]
    macs_choice = random.choice(choice_ls)
    while your_choice == macs_choice:     # 输入直到没有平局
            your_choice = input("Draw. Please input again:")
    else:
        print(f"your choice is {your_choice},Mac's choice is {macs_choice}")
        if [your_choice, macs_choice] in win_ls:
            return True   # 返回 True、False 更方便后面的判断
        else:             # 只可惜和程序不兼容
            return False





""" 用随机数实现内置的选择 """
import random
dit={0:'石头',1:'剪刀',2:'布'}   # 用字典建立内置的映射

""" 用户输入的对应关系 """
dct={'石头':0,'剪刀':1,'布':2,'R':0,'S':1,'P':'2','r':0,'s':1,'p':2}

money=100

""" 主要是避免Ctrl+C退出的错误 """
try:
    Begin()
except:
    pass
else:
    print("Perfect Run :)")
finally:
    print("Have Fun :)")


