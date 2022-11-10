from pico2d import *
import game_framework
import game_world

from grass import Grass
from boy import Boy
from ball import Ball, BigBall

boy = None
grass = None
balls = []
bigballs = []


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            boy.handle_event(event)


# 초기화
def enter():
    global boy, grass
    boy = Boy()
    grass = Grass()
    game_world.add_object(grass, 0)
    game_world.add_object(boy, 1)

    global balls, bigballs
    balls = [Ball() for i in range(10)] + [BigBall() for i in range(10)]

    game_world.add_objects(balls, 1)
    # game_world.add_objects(bigballs, 1)


    # 충돌 그룹 정보 추가
    # 소년과 볼들의 충돌 그룹 추가
    game_world.add_collision_group(boy, balls, 'boy:ball')
    game_world.add_collision_group(grass, balls, 'grass:ball')
    # game_world.add_collision_group(grass, bigballs, 'grass:ball')

    # 땅과 볼들의 충돌 그룹 추가


# 종료
def exit():
    game_world.clear()

def update():
    for game_object in game_world.all_objects():
        game_object.update()

    # 충돌체크
    for a, b, group in game_world.all_collision_pairs():
        if collide(a, b):
            print('COLLISION', group)
            a.handle_collision(b, group)
            b.handle_collision(a, group)
        pass

    # for ball in balls.copy():
    #     if collide(boy, ball):
    #         print("COLLISION boy:ball")
    #         balls.remove(ball)
    #         game_world.remove_object(ball)

def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    pass

def resume():
    pass


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


def test_self():
    import play_state

    pico2d.open_canvas()
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
