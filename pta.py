import collections
import re
topic_cnt = {}
hot_cnt = collections.OrderedDict()
pattern1 = re.compile(r"#.+#")

for i in range(int(input())):
    ls = pattern1.findall(input())
    s = ''
    for i in ls:
        s = i.replace('!', '').replace('.', '').capitalize()

    sr = s.replace('#', '')
    topic_cnt[sr] = topic_cnt.get(sr, 0)+1
    ss = s.split("#")
    for i in ss:
        if i != '' and i != ' ':
            hot_cnt[i] = hot_cnt.get(i, 0)+1
max = 0
name = ''
hot_cnt = sorted(hot_cnt.items(), key=lambda d: d[0], reverse=False)
print(hot_cnt)
for i, j in hot_cnt:
    if j > max:
        name = i
        max = j
print(name.capitalize())

pattern2 = re.compile(f"{name}")
for i in topic_cnt:
    if pattern2.findall(i):
        print(topic_cnt[i])
        break

print(f"And {len(hot_cnt)-1} more ...")
