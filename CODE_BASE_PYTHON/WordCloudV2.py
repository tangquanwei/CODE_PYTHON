import jieba  # 词语切割
import matplotlib.pyplot as plt  # 数据可视化
import numpy as np  # 科学计算
import wordcloud  # 分词
from PIL import Image  # 处理图片
from wordcloud import STOPWORDS, ImageColorGenerator, WordCloud  # 词云，颜色生成器，停止词


def ciyun():
    with open('少年中国说.txt', 'r', encoding='gbk') as f:  # 打开新的文本转码为gbk
        textfile = f.read()  # 读取文本内容
    wordlist = jieba.lcut(textfile)  # 切割词语
    space_list = ' '.join(wordlist)  # 空格链接词语
    # print(space_list)
    backgroud = np.array(Image.open('test2.jpg'))

    wc = WordCloud(width=1400, height=2200,
                   background_color='white',
                   mode='RGB',
                   mask=backgroud,  # 添加蒙版，生成指定形状的词云，并且词云图的颜色可从蒙版里提取
                   max_words=500,
                   stopwords=STOPWORDS,  # 内置的屏蔽词,并添加自己设置的词语
                   font_path='C:\Windows\Fonts\STZHONGS.ttf',
                   max_font_size=150,
                   relative_scaling=0.6,  # 设置字体大小与词频的关联程度为0.4
                   random_state=50,
                   scale=2
                   ).generate(space_list)

    image_color = ImageColorGenerator(backgroud)  # 设置生成词云的颜色，如去掉这两行则字体为默认颜色
    wc.recolor(color_func=image_color)

    plt.imshow(wc)  # 显示词云
    plt.axis('off')  # 关闭x,y轴
    plt.show()  # 显示
    wc.to_file('test2_ciyun.jpg')  # 保存词云图


def main():
    ciyun()


if __name__ == '__main__':
    main()


def read_stopword(fpath):
    # 读取中文停用词表
    with open(fpath, 'r', encoding='utf-8') as file:
        stopword = file.readlines()
    return [word.replace('\n', '') for word in stopword]


# 加载多个停用词表
path = 'E:\WeChatPublicNumber\python\词云图\stopwords'
# 前两个停用词表是网上下载的，第三个是自己设置的
name_list = ['中文停用词.txt', '哈工大停用词.txt', 'stopword.txt']

stop_word = []
for fname in name_list:
    stop_word += read_stopword(os.path.join(path, fname))
stop_word = set(stop_word)
