from pico2d import*
from enum import Enum

open_canvas()
Porygon = load_image('Porygon.png')
Background = load_image('background.png')

class Porygon_Vec(Enum):
    S = 0
    SE = 1
    E = 2
    NE = 3
    N = 4
    NW = 5
    W = 6
    SW = 7

def drawObject():
    clear_canvas()
    Background.draw(400, 300)

def getHeading(heading):
    if heading == Porygon_Vec.S:
        return 0
    elif heading == Porygon_Vec.SE:
        return 1
    elif heading == Porygon_Vec.E:
        return 2
    elif heading == Porygon_Vec.NE:
        return 3
    elif heading == Porygon_Vec.N:
        return 4
    elif heading == Porygon_Vec.NW:
        return 5
    elif heading == Porygon_Vec.W:
        return 6
    elif heading == Porygon_Vec.SW:
        return 7


def idle(x, y, heading):
    print('idle func working')
    for i in range(0, 5):
        drawObject()
        Porygon.clip_draw(1 + getHeading(heading)*29, 9*29 + 1, 28, 28, x, y + (i % 2)*2)
        update_canvas()
        delay(0.25)
        get_events()


def move(x, y, heading):
    print('move func working')
    frame = 0
    for i in range(0, 10):
        drawObject()
        if heading == Porygon_Vec.S:
            y -= 10
        elif heading == Porygon_Vec.SE:
            x += 10
            y -= 10
        elif heading == Porygon_Vec.E:
            x += 10
        elif heading == Porygon_Vec.NE:
            x+=10
            y+=10
        elif heading == Porygon_Vec.N:
            y+=10
        elif heading == Porygon_Vec.NW:
            x-=10
            y+=10
        elif heading == Porygon_Vec.W:
            x-=10
        elif heading == Porygon_Vec.SW:
            x-=10
            y-=10

        Porygon.clip_draw(1 + frame*29, (7 - getHeading(heading))*29 + 1, 28, 28, x, y)
        frame = (frame + 1) % 4
        update_canvas()
        delay(0.25)
        get_events()


def attack(x, y, heading):
    print('attack func working')
    undo = False
    for i in range(0, 10):
        drawObject()
        if i%2 == 0:
            undo = False
        else:
            undo = True

        if heading == Porygon_Vec.S:
            if not undo:
                y -= 10
            else:
                y += 10
        elif heading == Porygon_Vec.SE:
            if not undo:
                x += 10
                y -= 10
            else:
                x -= 10
                y += 10
        elif heading == Porygon_Vec.E:
            if not undo:
                x += 10
            else:
                x -= 10
        elif heading == Porygon_Vec.NE:
            if not undo:
                x+=10
                y+=10
            else:
                x-=10
                y-=10
        elif heading == Porygon_Vec.N:
            if not undo:
                y+=10
            else:
                y-=10
        elif heading == Porygon_Vec.NW:
            if not undo:
                x-=10
                y+=10
            else:
                x+=10
                y-=10
        elif heading == Porygon_Vec.W:
            if not undo:
                x-=10
            else:
                x+=10
        elif heading == Porygon_Vec.SW:
            if not undo:
                x-=10
                y-=10
            else:
                x+=10
                y+=10
        Porygon.clip_draw(1 + (4-i%2)*29, (7 - getHeading(heading))*29 + 1, 28, 28, x, y)
        update_canvas()
        delay(0.25)
        get_events()

def hurt(x, y, heading):
    print('hurt func working')
    xOffset = 3
    for i in range(0, 10):
        drawObject()
        if i%2 == 0:
            xOffset = 3
            #y-=5
        else:
            xOffset = 5
            #y+=5
        drawObject()
        Porygon.clip_draw(1 + xOffset*29, (7 - getHeading(heading))*29 + 1, 28, 28, x, y)
        update_canvas()
        delay(0.25)
        get_events()

#모든 움직임을 묶어둔 함수
def moveSet():
    attack(x, y, heading)
    hurt(x, y, heading)
    idle(x, y, heading)
    move(x, y, heading)


x = 400
y = 300

while True:
    heading = Porygon_Vec.S
    moveSet()

    heading = Porygon_Vec.SE
    moveSet()

    heading = Porygon_Vec.E
    moveSet()

    heading = Porygon_Vec.NE
    moveSet()

    heading = Porygon_Vec.N
    moveSet()

    heading = Porygon_Vec.NW
    moveSet()

    heading = Porygon_Vec.W
    moveSet()

    heading = Porygon_Vec.SW
    moveSet()

close_canvas()
