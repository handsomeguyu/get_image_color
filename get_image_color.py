# import colorsys
# from PIL import Image
#
#
# def get_dominant_color(image):
# #颜色模式转换，以便输出rgb颜色值
#     image = image.convert('RGBA')
# #生成缩略图，减少计算量，减小cpu压力
#     image.thumbnail((200, 200))
#     max_score = 0.0
#     dominant_color = None
#     for count, (r, g, b, a) in image.getcolors(image.size[0] * image.size[1]):
#         # 跳过纯黑色
#         if a == 0:
#             continue
#         saturation = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)[1]
#         y = min(abs(r * 2104 + g * 4130 + b * 802 + 4096 + 131072) >> 13, 235)
#         y = (y - 16.0) / (235 - 16)
#         # 忽略高亮色
#         if y > 0.9:
#             continue
#         # Calculate the score, preferring highly saturated colors.
#         # Add 0.1 to the saturation so we don't completely ignore grayscale
#         # colors by multiplying the count by zero, but still give them a low
#         # weight.
#         score = (saturation + 0.1) * count
#         if score > max_score:
#             max_score = score
#             dominant_color = r, g, b
#     return dominant_color
#
#
# def RGB_to_Hex(rgb):
#     RGB = rgb.split(', ')            # 将RGB格式划分开来
#     color = '#'
#     for i in RGB:
#         num = int(i)
#         # 将R、G、B分别转化为16进制拼接转换并大写  hex() 函数用于将10进制整数转换成16进制，以字符串形式表示
#         color += str(hex(num))[-2:].replace('x', '0').upper()
#     print(color)
#     return color
#
#
# if __name__ == '__main__':
#     print(str(get_dominant_color(Image.open('front.png')))[:-1][1:])
#     print(str(get_dominant_color(Image.open('rear.png')))[:-1][1:])
#     print(str(get_dominant_color(Image.open('left.png')))[:-1][1:])
#     print(str(get_dominant_color(Image.open('right.png')))[:-1][1:])
#     color_front = RGB_to_Hex(str(get_dominant_color(Image.open('front.png')))[:-1][1:])
#     color_rear = RGB_to_Hex(str(get_dominant_color(Image.open('rear.png')))[:-1][1:])
#     color_left = RGB_to_Hex(str(get_dominant_color(Image.open('left.png')))[:-1][1:])
#     color_right = RGB_to_Hex(str(get_dominant_color(Image.open('right.png')))[:-1][1:])
#
#

import cv2
import numpy as np

import collections


# 定义字典存放颜色分量上下限
# 例如：{颜色: [min分量, max分量]}
# {'red': [array([160,  43,  46]), array([179, 255, 255])]}

def getColorList():
    dict = collections.defaultdict(list)

    # 黑色
    lower_black = np.array([0, 0, 0])
    upper_black = np.array([180, 255, 46])
    color_list = []
    color_list.append(lower_black)
    color_list.append(upper_black)
    dict['black'] = color_list

    # #灰色
    # lower_gray = np.array([0, 0, 46])
    # upper_gray = np.array([180, 43, 220])
    # color_list = []
    # color_list.append(lower_gray)
    # color_list.append(upper_gray)
    # dict['gray']=color_list

    # 白色
    lower_white = np.array([0, 0, 221])
    upper_white = np.array([180, 30, 255])
    color_list = []
    color_list.append(lower_white)
    color_list.append(upper_white)
    dict['white'] = color_list

    # 红色
    lower_red = np.array([156, 43, 46])
    upper_red = np.array([180, 255, 255])
    color_list = []
    color_list.append(lower_red)
    color_list.append(upper_red)
    dict['red'] = color_list

    # 红色2
    lower_red = np.array([0, 43, 46])
    upper_red = np.array([10, 255, 255])
    color_list = []
    color_list.append(lower_red)
    color_list.append(upper_red)
    dict['red2'] = color_list

    # 橙色
    lower_orange = np.array([11, 43, 46])
    upper_orange = np.array([25, 255, 255])
    color_list = []
    color_list.append(lower_orange)
    color_list.append(upper_orange)
    dict['orange'] = color_list

    # 黄色
    lower_yellow = np.array([26, 43, 46])
    upper_yellow = np.array([34, 255, 255])
    color_list = []
    color_list.append(lower_yellow)
    color_list.append(upper_yellow)
    dict['yellow'] = color_list

    # 绿色
    lower_green = np.array([35, 43, 46])
    upper_green = np.array([77, 255, 255])
    color_list = []
    color_list.append(lower_green)
    color_list.append(upper_green)
    dict['green'] = color_list

    # 青色
    lower_cyan = np.array([78, 43, 46])
    upper_cyan = np.array([99, 255, 255])
    color_list = []
    color_list.append(lower_cyan)
    color_list.append(upper_cyan)
    dict['cyan'] = color_list

    # 蓝色
    lower_blue = np.array([100, 43, 46])
    upper_blue = np.array([124, 255, 255])
    color_list = []
    color_list.append(lower_blue)
    color_list.append(upper_blue)
    dict['blue'] = color_list

    # 紫色
    lower_purple = np.array([125, 43, 46])
    upper_purple = np.array([155, 255, 255])
    color_list = []
    color_list.append(lower_purple)
    color_list.append(upper_purple)
    dict['purple'] = color_list

    return dict


# 处理图片
def get_color(frame):
    print('go in get_color')
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    maxsum = -100
    color = None
    color_dict = getColorList()
    for d in color_dict:
        mask = cv2.inRange(hsv, color_dict[d][0], color_dict[d][1])
        cv2.imwrite(d + '.jpg', mask)
        binary = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)[1]
        binary = cv2.dilate(binary, None, iterations=2)
        img, cnts = cv2.findContours(binary.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        sum = 0
        for c in cnts:
            sum += cv2.contourArea(c)
        if sum > maxsum:
            maxsum = sum
            color = d

    return color


if __name__ == '__main__':
    frame = cv2.imread('front.jpg')
    print(get_color(frame))
