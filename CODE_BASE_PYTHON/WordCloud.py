import jieba
import wordcloud
import scipy.misc

mask = scipy.misc.imread("2.png")
fo = open("./txts/words.txt", "r", encoding="utf-8")
t = fo.read()
fo.close()
ls = jieba.lcut(t)
n = len(ls) - 1
while n > 0:
    if len(ls[n]) == 1:
        del ls[n]
    n = n-1
txt = " ".join(ls)
c = wordcloud.WordCloud(width=1000, font_path="msyh.ttc", mask=mask,
                        height=700, background_color="white")
c.generate(txt)
c.to_file("b.png")
