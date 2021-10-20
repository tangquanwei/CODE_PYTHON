# -*- coding:utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os
import sys
import shutil


class Video2Ascii:

    def __init__(self, filename):
        # 执行前的一些判断
        if not os.path.isfile(filename):
            print("源文件找不到，或者不存在！")
            exit()

        temp_arr = filename.split('.')

        # 字符列表，从左至右逐渐变得稀疏，对应着颜色由深到浅
        self.ascii_char = list("$@B%8&WM#*oahkbdpqwO0QLCJYXzcvunxrjft/\|()1[]?-_+~<>i!......... ")

        # 传入视频文件名
        self.filename = filename
        # 输出视频文件名
        self.outname = temp_arr[0] + "_out." + temp_arr[1]

        # 存储图片的临时路径、输出路径
        self.pic_path = 'temp_pic'
        self.ascii_path = 'temp_ascii'
        self.outpath = 'temp_out'

        # 设置图片缩小的倍数
        self.resize_times = 6

        # 设置输出文件的名字,声音文件以及带声音的输出文件
        self.mp3ilename = os.path.join(self.outpath, temp_arr[0] + '.mp3')
        self.mp4filename = os.path.join(self.outpath, self.outname)

        # 合并输出的视频文件
        self.mergefilename = os.path.join(self.outpath, temp_arr[0] + '_voice.' + temp_arr[1])

    # [1]、创建存储临时图片的路径
    def createpath(self):
        print("-" * 30)
        print("[1/6]正在创建临时路径...")
        print("-" * 30 + '\r\n')

        # 源视频文件的图片路径
        if not os.path.exists(self.pic_path):
            os.makedirs(self.pic_path)
        else:
            # 清空在创建
            shutil.rmtree(self.pic_path)
            os.makedirs(self.pic_path)

        # 转换之后的图片路径
        if not os.path.exists(self.ascii_path):
            os.makedirs(self.ascii_path)
        else:
            # 清空再创建
            shutil.rmtree(self.ascii_path)
            os.makedirs(self.ascii_path)

        # 存储输出文件的目录
        if not os.path.exists(self.outpath):
            os.makedirs(self.outpath)

    # [2]、将视频分割成图片
    def video2pic(self):
        print("-" * 30)
        print("[2/6]正在切割原始视频为图片...")
        print("-" * 30 + '\r\n')
        # 使用D:\ZIPS\ffmpeg-N-103179-gac0408522a-win64-gpl\bin\ffmpeg.exe切割图片，命令行如下
        cmd = 'D:\\ZIPS\\ffmpeg-N-103179-gac0408522a-win64-gpl\\bin\\ffmpeg.exe -i {0} -r 24 {1}/%06d.jpeg'.format(self.filename, self.pic_path)

        # 执行命令
        os.system(cmd)

    # [3]、将图片缩放、转成ascii形式
    def pic2ascii(self):
        print("-" * 30)
        print("[3/6]正在处理分析图片，转成ascii形式...")
        print("-" * 30 + '\r\n')
        # 读取原始图片目录
        pic_list = sorted(os.listdir(self.pic_path))

        total_len = len(pic_list)
        count = 1

        # 遍历每张图片
        for pic in pic_list:
            # 图片完整路径
            imgpath = os.path.join(self.pic_path, pic)

            # 1、缩小图片，转成灰度模式，存入数组
            origin_img = Image.open(imgpath)

            # 缩小之后宽高
            resize_width = int(origin_img.size[0] / self.resize_times)
            resize_height = int(origin_img.size[1] / self.resize_times)

            resize_img = origin_img.resize((resize_width, resize_height), Image.ANTIALIAS).convert("L")

            img_arr = np.array(resize_img)

            # 2、新建空白图片（灰度模式、与原始图片等宽高）
            new_img = Image.new("L", origin_img.size, 255)
            draw_obj = ImageDraw.Draw(new_img)
            font = ImageFont.truetype("arial.ttf", 8)

            # 3、将每个字符绘制在 8*8 的区域内
            for i in range(resize_height):
                for j in range(resize_width):
                    x, y = j*self.resize_times, i*self.resize_times
                    index = int(img_arr[i][j]/4)
                    draw_obj.text((x, y), self.ascii_char[index], font=font, fill=0)

            # 4、保存字符图片
            new_img.save(os.path.join('temp_ascii', pic), "JPEG")
            print("已生成ascii图（%d/%d）" % (count, total_len))
            count += 1

            # exit()

    # [4]、合成视频
    def ascii2video(self):
        print("-" * 30)
        print("[4/6]正在合成视频...")
        print("-" * 30 + '\r\n')
        # 输出视频保存路径
        savepath = os.path.join(self.outpath, self.outname)

        cmd = 'D:\\ZIPS\\ffmpeg-N-103179-gac0408522a-win64-gpl\\bin\\ffmpeg.exe -threads 2 -start_number 000001 -r 24 -i {0}/%06d.jpeg -vcodec mpeg4 {1}'.format(self.ascii_path, savepath)

        os.system(cmd)

    # [5]、获取原始视频的mp3文件
    def video2mp3(self):
        print("-" * 30)
        print("[5/6]正在分离音频文件...")
        print("-" * 30 + '\r\n')

        # mp3名字和保存路径
        name = self.filename.split('.')[0] + '.mp3'
        savepath = os.path.join(self.outpath, name)
        cmd = 'D:\\ZIPS\\ffmpeg-N-103179-gac0408522a-win64-gpl\\bin\\ffmpeg.exe -i {0} -f mp3 {1}'.format(self.filename, savepath)

        os.system(cmd)

    # [6]、将视频和音频合并
    def mp4andmp3(self):
        print("-"*30)
        print("[6/6]正在合并视频和音频...")
        print("-" * 30 + '\r\n')

        cmd = 'D:\\ZIPS\\ffmpeg-N-103179-gac0408522a-win64-gpl\\bin\\ffmpeg.exe -i {0} -i {1} -strict -2 -f mp4 {2}'.format(self.mp4filename, self.mp3ilename,  self.mergefilename)

        os.system(cmd)

    # [0]、启动
    def start(self):
        """
            > 程序流程：
                1、创建路径
                2、将原始视频分割成图片
                3、将图片缩放、转成ascii形式
                4、将ascii形式的图片合成视频
                5、获取音频mp3文件
                6、合并视频和音频文件
        :return:
        """
        self.createpath()
        self.video2pic()
        self.pic2ascii()
        self.ascii2video()

        self.video2mp3()
        self.mp4andmp3()

        print("程序执行完成")


if __name__ == "__main__":
    # if len(sys.argv) != 2:
    #     print("参数不匹配,请参考(脚本名 原始视频)：xxx.py test.mp4 ")
    #     exit()

    # demo = Video2Ascii(sys.argv[1])
    demo = Video2Ascii("test.mp4")
    demo.start()
    
