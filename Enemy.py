from pico2d import*
import random


class Enemy:
    PIXEL_PER_METER = (30.0 / 1.0)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 3.5                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.1
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    image = None

    UP, DOWN, LEFT, RIGHT = 0, 2, 4, 6

    def __init__(self, x, y, type):
        self.x, self.y = x, y
        self.type = type
        self.frame = random.randint(0, 3)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = 0
        self.state = random.randint(0, 3) * 2
        if Enemy.image == None:
            Enemy.image = load_image('png/ghost.png')

    def update(self, frame_time):
        self.life_time += frame_time
        distance = Enemy.RUN_SPEED_PPS * frame_time
        self.total_frames += Enemy.FRAMES_PER_ACTION * Enemy.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 8
       # self.x += (self.dir * distance)

    def draw(self):
        self.image.clip_draw(self.state* 30, self.type*30, 30, 30, self.x, self.y)