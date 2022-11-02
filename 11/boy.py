from pico2d import *

# 이벤트 정의
RD, LD, RU, LU, TIMER, AD = range(6)

key_evnet_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    # (SDL_KEYDOWN, SDLK_a): AU,
    (SDL_KEYUP, SDLK_a): AD
}


# 클래스를 이용해서 상태를 만든다
class IDLE:
    @staticmethod
    def enter(self, event):
        print('Enter Idle')
        self.dir = 0
        self.frame = 0

        self.timer = 1000
        pass

    @staticmethod
    def exit(self):
        print('Exit Idle')
        pass


    @staticmethod
    def do(self):
        self.frame = (self.frame+1) % 8
        self.timer -= 1
        if self.timer == 0:
            # self.q.insert(0, TIMER)
            self.add_event(TIMER)   # 객체지향적인 방법
        pass

    @staticmethod
    def draw(self):
        if self.face_dir == 1:  # 오른쪽을 바라보고 있는 상태
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)
        pass

class RUN:
    @staticmethod
    def enter(self, event):
        print('Enter Run')

        if event == RD: self.dir += 1
        elif event == LD: self.dir -= 1
        elif event == RU: self.dir -= 1
        elif event == LU: self.dir += 1

        pass

    @staticmethod
    def exit(self):
        print('Exit Run')
        # run을 나가서 idle로 갈 때, run의 방향을 알려줄 필요가 있다
        self.face_dir = self.dir
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        self.x = clamp(0, self.x, 800)      # x를 0, 800 사이 값으로 고정
        pass

    @staticmethod
    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        pass

class SLEEP:
    @staticmethod
    def enter(self, event):
        print('Enter Sleep')
        self.dir = 0
        self.frame = 0
        pass

    @staticmethod
    def exit(self):
        print('Exit Sleep')
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame+1) % 8
        pass

    @staticmethod
    def draw(self):
        if self.face_dir == 1:  # 오른쪽을 바라보고 있는 상태
            self.image.clip_composite_draw(self.frame * 100, 200, 100, 100,
                                           3.141592 / 2, '', self.x + 25, self.y - 25, 100, 100)
        else:
            self.image.clip_composite_draw(self.frame * 100, 200, 100, 100,
                                            -3.141592 / 2, '', self.x + 25, self.y - 25, 100, 100)
        pass

class AUTO_RUN:
    @staticmethod
    def enter(self, event):
        print('Enter Auto_run')
        self.dir = self.face_dir
        self.frame = 0
        pass

    @staticmethod
    def exit(self):
        print('Exit Auto_run')
        self.face_dir = self.dir
        self.dir = 0
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        if self.x > 800 or self.x < 0:
           self.dir *= -1
        pass

    @staticmethod
    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y + 35, 200, 200)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y + 35, 200, 200)
        pass


next_status = {
    SLEEP: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, AD: AUTO_RUN, SLEEP: SLEEP},
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, AD: AUTO_RUN, TIMER: SLEEP},
    RUN: {RU: IDLE, LU: IDLE, LD: IDLE, AD: AUTO_RUN, RD: IDLE},
    AUTO_RUN: {RU: AUTO_RUN, LU: AUTO_RUN, RD: RUN, LD: RUN, AD: IDLE},
}

class Boy:
    def __init__(self):
        self.x, self.y = 0, 85
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')
        
        # 상태처리를 위한 큐
        self.q = []
        # 현재 상태를 IDLE로 초기화 후 enter() 호출
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        # 현재 상태가 뭔지 모르지만 실행해라
        self.cur_state.do(self)

        if self.q: # q에 뭔가 들어있다면
            event = self.q.pop()        # 이벤트를 가져오고,
            self.cur_state.exit(self)       # 현재 상태를 나가고,
            self.cur_state = next_status[self.cur_state][event] # 다음 상태를 계산함
            self.cur_state.enter(self, event)
        # self.frame = (self.frame + 1) % 8
        # self.x += self.dir * 1
        # self.x = clamp(0, self.x, 800)

    def draw(self):
        self.cur_state.draw(self)
        # if self.dir == -1:
        #     self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        # elif self.dir == 1:
        #     self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        # else:
        #     if self.face_dir == 1:
        #         self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        #     else:
        #         self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)

    def add_event(self, event):
        self.q.insert(0, event)

    def handle_event(self, event): # 객체지향을 위해 여기서 직접 이벤트 관리, 소년이 스스로 이벤트를 처리할 수 있게
        # event 는 키이벤트, 이것을 내부 RD등으로 변환
        if (event.type, event.key) in key_evnet_table:
            key_event = key_evnet_table[(event.type, event.key)]
            self.add_event(key_event) # 변환된 내부 이벤트를 큐에 추가


        # if event.type == SDL_KEYDOWN:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             self.dir -= 1
        #         case pico2d.SDLK_RIGHT:
        #             self.dir += 1
        # elif event.type == SDL_KEYUP:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             self.dir += 1
        #             self.face_dir = -1
        #         case pico2d.SDLK_RIGHT:
        #             self.dir -= 1
        #             self.face_dir = 1