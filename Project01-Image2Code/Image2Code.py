#!/usr/bin/env python
# coding:utf-8

from PIL import Image
import argparse
'''
    argparse:命令行参数解析模块。
    
'''

#创建解析对象
parser = argparse.ArgumentParser()

'''
添加需要关注的命令和选项，每一个add_argument都表示要添加一个要关注的命令和选项
不带'--'的参数，调用脚本时必须要输入值，参数输入的顺序与程序中定义的顺序一致
带'-'的参数，可以不输入add_argument('-a')，程序中变量名为定义的参数名
带'--'的参数:
    参数别名，例如：add_argument('-shortname','--name',help='params means')
        -shortname:系统中的名称  --name:自定义的名称  help:作用解释
        代码中使用，不能使用shortname
    dest:参数在程序中对应的变量名称  add_argument('a',dest='code_name')
    default:参数默认值
    help:参数作用解释  add_argument('a',help='params means')
    type:默认string  add_argument('c',type=int)
    action:
        store:默认action模式，存储值到指定变量
        store_const:存储值在参数的const部分指定，多用于实现非布尔的命令行flag
        store_true / store_false：布尔开关。可以2个参数对应一个变量。
        append：存储值到列表，该参数可以重复使用。
        append_const：存储值到列表，存储值在参数的const部分指定。
        count: 统计参数简写输入的个数  add_argument("-c", "--gc", action="count")
        version 输出版本信息然后退出。
    const:配合action="store_const|append_const"使用，默认值
    choices:输入值的范围 add_argument("--gb", choices=['A', 'B', 'C', 0])
    
    使用：python3 ascii.py oo.png --width 100 --height 80  后面的宽高是可以自定义，也可以不输，默认80*80
'''
parser.add_argument('file')
#-i -o选项来区别参数是输入文件还是输出文件
parser.add_argument('-o','--output')
parser.add_argument('--width',type=int,default=80)
parser.add_argument('--height',type=int,default=80)

#开始解析
args = parser.parse_args()

#获取解析出来的数据
IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

#输出的全部字符串
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'.")

#获得字符串，输入rgba值
def get_char(r,g,b,alpha=256):
    #a为0，为空
    if alpha == 0:
        return ' '
    #输出字符串数组整体的长度
    length = len(ascii_char)
    #计算灰度
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    #透明度与全部字符长度的比例
    unit = (256.0 + 1)/length
    #返回当前点的字符
    return ascii_char[int(gray/unit)]

#如果是主函数
if __name__ == '__main__':
    #利用PIL打开图片
    im = Image.open(IMG)
    #按照新的尺寸拷贝出原图片
    im = im.resize((WIDTH,HEIGHT),Image.NEAREST)

    txt = ""

    #遍历高度
    for i in range(HEIGHT):
        #遍历宽度
        for j in range(WIDTH):
            #获得该点的像素
            pixel = im.getpixel((j,i))
            #获得字符串并拼接
            txt += get_char(*pixel)
        #结束后添加换行符
        txt += '\n'

    #打印结果
    print(txt)

    #如果有指定输出
    if OUTPUT:
        #输出到该文件
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        #没有指定输出，输出到当前目录下
        with open('output.txt','w') as f:
            f.write(txt)
