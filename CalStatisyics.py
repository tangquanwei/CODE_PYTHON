# CalStatisticsV1
from typing import Sized


def getNum():
    nums = []
    iNumStr = input("请输入数字（回车退出）：")
    while iNumStr != "":
        nums.append(eval(iNumStr))
        iNumStr = input("请输入数字（回车退出）：")
    return nums

def mean(numbers):
    s=0.0
    for num in numbers:
        s += num
    return s/len(numbers)

def dev(numbers,mean): #方差
    sdev = 0.0
    for num in numbers:
        sdev += (num - mean)**2
    return pow(sdev / (len(numbers)-1),0.5)

def media(numbers):
    sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        med = (numbers[size//2-1] + numbers[size//2])
    else:
        med = numbers[size//2]
    return med

n = getNum()
m = mean(n)
print("这{}个数的平均值是：{}，方差是：{:.2f}，中位数数是：{}\n".format(len(n),m,dev(n,m),media(n)))
