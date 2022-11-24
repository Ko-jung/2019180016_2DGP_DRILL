from pico2d import *
import game_world
import random

import server


class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(100, 1600), random.randint(100, 1000)
        # self.x, self.y = random.randint(0, 800 * 3), random.randint(0, 600 * 3)
        print(f'new ball {self.x, self.y = }')

    def draw(self):
        if server.background.window_left < self.x < server.background.window_left + server.background.canvas_width and server.background.window_bottom < self.y < server.background.window_bottom  + server.background.canvas_height:
            self.image.draw(self.x - server.background.window_left, self.y - server.background.window_bottom)
            print(f'{server.background.window_left, server.background.window_bottom}')
            # draw_rectangle(*(self.get_bb()))

    def update(self):
        pass

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, other, group):
        if group == 'boy:ball':
            game_world.remove_object(self)
