from pico2d import *
KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    global running
    global dirx
    global diry
    global character_status

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            # if character_status == 2:
            #     character_status = 0
            # elif character_status == 3:
            #     character_status = 1
            if event.key == SDLK_RIGHT:
                dirx += 1
                #character_status = 1
            elif event.key == SDLK_LEFT:
                dirx -= 1
                #character_status = 0
            if event.key == SDLK_UP:
                diry += 1
            elif event.key == SDLK_DOWN:
                diry -= 1
            elif event.key == SDLK_ESCAPE:
                running = False

            if dirx > 0:
                character_status = 1
            elif dirx < 0:
                character_status = 0
            elif dirx == 0:
                if character_status == 2:
                    character_status = 0
                elif character_status == 3:
                    character_status = 1



        elif event.type == SDL_KEYUP:
            # if character_status == 0:
            #     character_status = 2
            # elif character_status == 1:
            #     character_status = 3
            if event.key == SDLK_RIGHT:
                character_status = 3
                dirx -= 1
            elif event.key == SDLK_LEFT:
                character_status = 2
                dirx += 1
            if event.key == SDLK_UP:
                diry -= 1
            elif event.key == SDLK_DOWN:
                diry += 1

            if dirx > 0:
                character_status = 1
            elif dirx < 0:
                character_status = 0
            elif dirx == 0:
                if character_status == 0:
                    character_status = 2
                elif character_status == 1:
                    character_status = 3


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')


running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
character_status = 2
# 3 = right_idle, 2 = left_idle, 1 = right_run, 0 = left_run
dirx = 0
diry = 0

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, character_status * 100, 100, 100, x, y)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8

    x += dirx * 5
    y += diry * 5
    if x < 0 or x > KPU_WIDTH:
        x -= dirx * 5
    if y < 0 or y > KPU_HEIGHT:
        y -= diry * 5
    #elay(0.05)

close_canvas()

