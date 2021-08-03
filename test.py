# “两个集合都有的不相等整数的个数”意思是两个集合的交集个数，\
# “两个集合一共有的不相等整数的个数”意思是先将两个集合并起来再去重得到的集合元素个数
n = int(input())
ls1 = []
ls2 = []
for i in range(n):
    ls1.append(input()[1:].split())
k = int(input())
for i in range(k):
    ls2.append(tuple(map(int,input().split())))
for i in range(k):
    s1=set(ls1[ls2[i][0]-1])
    s2=set(ls1[ls2[i][1]-1])
    print(f"{len(s1&s2)/len(s1|s2)*100:.2f}%",end='\n'if i!=k-1 else '')
