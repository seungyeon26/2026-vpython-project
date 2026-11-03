Web VPython 3.2

x= ''
import random
box(pos = vec(0, 0, 0), length = 3, height = 2, width = 0.2, texture = "https://i.postimg.cc/0NR1rqBL/hwamyeon-kaebcheo-2026-11-03-152035.png")
label(pos = vec(-1.2, 0.14, 0), text = random.randint(1, 35), xoffset = 20, yoffset = 50, space = 30, height = 40, border = 4, font = 'sans')
l1 = label(pos = vec(-0.15, 0.14, 0), text = x, xoffset = 20, yoffset = 50, space = 30, height = 40, border = 4, font = 'sans')
label(pos = vec(0.9, 0.14, 0), text = random.randint(1, 35), xoffset = 20, yoffset = 50, space = 30, height = 40, border = 4, font = 'sans')

while True :
    rate(100)
    k = keysdown()
    if ' ' in k :
        x = input()
        l1.text = x   
