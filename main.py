import cv2
import numpy as np
import colorList

# filename = 'right.png'


# 处理图片
def get_color(frame):
    # print('go in get_color')
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    maxsum = -100
    color = None
    color_dict = colorList.getColorList()
    for d in color_dict:
        mask = cv2.inRange(hsv, color_dict[d][0], color_dict[d][1])
        # cv2.imwrite(d + '.png', mask)
        binary = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)[1]
        binary = cv2.dilate(binary, None, iterations=2)
        cnts, hiera = cv2.findContours(binary.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        sum = 0
        for c in cnts:
            sum += cv2.contourArea(c)
        if sum > maxsum:
            maxsum = sum
            color = d

    return color


if __name__ == '__main__':
    frame_front = cv2.imread('front.png')
    frame_rear = cv2.imread('rear.png')
    frame_left = cv2.imread('left.png')
    frame_right = cv2.imread('right.png')
    print(get_color(frame_front))
    print(get_color(frame_rear))
    print(get_color(frame_left))
    print(get_color(frame_right))
