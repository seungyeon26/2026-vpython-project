Web VPython 3.2

x= ''
box(pos = vec(0, 0, 0), length = 3, height = 2, width = 0.2, texture = "https://i.postimg.cc/0NR1rqBL/hwamyeon-kaebcheo-2026-11-03-152035.png")
label(pos = vec(-1.2, 0.14, 0), text = '77', xoffset = 20, yoffset = 50, space = 30, height = 40, border = 4, font = 'sans')
l1 = label(pos = vec(-0.15, 0.14, 0), text = x, xoffset = 20, yoffset = 50, space = 30, height = 40, border = 4, font = 'sans')
label(pos = vec(0.9, 0.14, 0), text = '135', xoffset = 20, yoffset = 50, space = 30, height = 40, border = 4, font = 'sans')


head = sphere(pos = vec(-1.1, 0, 0.2), radius = 0.13)
body = box(pos = vec(-1.1, -0.4, 0.2), length = 0.3, height = 0.5, width = 0.17)
rightleg = box(pos = vec(-1.16, -0.6, 0.2), length = 0.06, height = 0.4, width = 0.1)
leftleg = box(pos = vec(-1.04, -0.6, 0.2), length = 0.06, height = 0.4, width = 0.1)
rightarm = box(pos = vec(-1.3, -0.07, 0.2), axis = vec(1, 0, 0), length = 0.06, height = 0.3, width = 0.1)
leftarm = box(pos = vec(-0.9, -0.07, 0.2), axis = vec(1, 0, 0), length = 0.06, height = 0.3, width = 0.1)
doll = compound([head, body, rightleg, leftleg, rightarm, leftarm])

d = doll

while True :
    rate(100)
    k = keysdown()
    if ' ' in k :
        x = input()
        l1.text = x   
    rate(25)
    k = keysdown()
    if 'left' in k : 
        d.pos.x -= 0.1
    if 'right' in k : 
        d.pos.x += 0.1
    if 'up' in k : 
        d.pos.y += 0.1
    if 'down' in k : 
        d.pos.y -= 0.1
    if x == '58' : 
        d.color = color.green
    else : 
        d.color = color.red


