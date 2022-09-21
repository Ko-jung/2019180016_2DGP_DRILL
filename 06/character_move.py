from pico2d import *
import math

def draw_png(x, y):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

circle = False
canChange = False

x = 400
y = 90
charMove = 0
#0 = right, 1 = up, 2 = left, 3 = down
count = 0

draw_png(x, y)

while(True):
    if circle:
        while count < 360:
            x = 300 * math.sin((180 + count) / 360 * 2 *math.pi) + 400
            y = 210 * math.cos((180 + count) / 360 * 2 *math.pi) + 300
            draw_png(x, y)
            delay(0.01)
            count += 1
        circle = False
        x = 400
        y = 90
        charMove = 0
        count = 0
        canChange = False
    else:
        if charMove == 0:
            while x < (800 - 21):# - character.w.x//2):
                x += 4
                draw_png(x, y)
                delay(0.01)
                if canChange and x > 400:
                    circle = True
                    x = 400
                    y = 90
                    charMove = 0
                    count = 0
                    canChange = False
                    break
            charMove = 1
        elif charMove == 1:
            while y < (600 - 46):# - character.w.y//2):
                y += 4
                draw_png(x, y)
                delay(0.01)
            charMove = 2
        elif charMove == 2:
            while x > 0 + 21:
                x -= 4
                draw_png(x, y)
                delay(0.01)
            charMove = 3
        elif charMove == 3:
            while y > 40 + 46:
                y -= 4
                draw_png(x, y)
                delay(0.01)
            charMove = 0
            canChange = True

close_canvas()
