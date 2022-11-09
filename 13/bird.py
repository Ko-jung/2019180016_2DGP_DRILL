from pico2d import *
import game_framework
import game_world
from ball import Ball
import random

#1 : 이벤트 정의
RD, LD, RU, LU, TIMER, SPACE = range(6)
event_name = ['RD', 'LD', 'RU', 'LU', 'TIMER', 'SPACE']

key_event_table = {
    (SDL_KEYDOWN, SDLK_SPACE): SPACE,
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU
}


#2 : 상태의 정의
class FLY:
    @staticmethod
    def enter(self,event):
        print('ENTER IDLE')
        self.dir = self.face_dir
        self.timer = 1000

    @staticmethod
    def exit(self, event):
        print('EXIT IDLE')
        if event == SPACE:
            self.fire_ball()

    def do(self):
        self.frame = (self.frame + self.FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        if self.x > 1600 or self.x < 0:
            self.dir *= -1
            self.face_dir *= -1


    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw((int(self.frame)) % 5 * (int)(918/5), (2 - int(self.frame) // 5)  * 504//3, (int(918/5)), 504//3, self.x, self.y, 100, 100)
        else:
            self.image.clip_composite_draw((int(self.frame)) % 5 * (int)(918/5), (2 - int(self.frame) // 5)  * 504//3, (int(918/5)), 504//3, 0, 'h', self.x, self.y, 100, 100)

# Boy Run Speed
PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KPH = 123.0
RUN_SPEED_MPM = RUN_SPEED_KPH * 1000 / 60
RUN_SPEED_MPS = RUN_SPEED_MPM / 60.0
RUN_SPEED_PPS = RUN_SPEED_MPS * PIXEL_PER_METER

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION

class Bird:
    def __init__(self, x = 800, y = 20):
        self.x, self.y = x, y
        self.frame = 0
        self.dir, self.face_dir = 1, 1
        self.image = load_image('bird_animation.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.FRAMES_PER_ACTION = random.randint(5,9)

        self.timer = 100

        self.event_que = []
        self.cur_state = FLY
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

        # if self.event_que:
        #     event = self.event_que.pop()
        #     self.cur_state.exit(self, event)
        #     try:
        #         self.cur_state = next_state[self.cur_state][event]
        #     except KeyError:
        #         print(f'ERROR: State {self.cur_state.__name__}    Event {event_name[event]}')
        #     self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        self.font.draw(self.x - 60, self.y + 50, f'(Time: {get_time():.2f})', (255, 255, 0))

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)