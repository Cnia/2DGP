from pico2d import*

class Player:

    PIXEL_PER_METER = (30.0 / 1.0)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 5  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4

    image = None

    RIGHT, LEFT, UP, DOWN = 3, 2, 1, 0

    def __init__(self):
        self.x, self.y = 40, 37
        self.frame = 0
        self.life_time = 0.0
        self.total_frames = 0.0
        self.state = self.RIGHT

        self.dirX = 0
        self.dirY = 0
        self.switch = 0
        self.collision = 0
        self.life = 3
        self.death_count = 0
        if Player.image == None:
            Player.image = load_image('resource/png/pacman.png')

    def update(self, frame_time):
        self.life_time += frame_time
        distance = Player.RUN_SPEED_PPS * frame_time
        self.total_frames += Player.FRAMES_PER_ACTION * Player.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 4
        self.x += (self.dirX * distance)
        self.y += (self.dirY * distance)

    def draw(self):
        if self.death_count == 0:
            self.image.clip_draw(self.frame * 20, self.state * 20, 20, 20, self.x, self.y)
        else:
            self.image.clip_draw(self.death_count * 20, self.state * 20, 20, 20, self.x, self.y)

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
                self.state = self.LEFT
                self.dirX = -1
                self.dirY = 0
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
                self.state = self.RIGHT
                self.dirX = 1
                self.dirY = 0
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
                self.state = self.UP
                self.dirX = 0
                self.dirY = 1
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
                self.state = self.DOWN
                self.dirX = 0
                self.dirY = -1

    def death(self):
        for i in range(11):
            self.death_count += 1
            self.draw()
            delay(0.2)
        self.life -= 1
        self.x = 40
        self.y = 37
        self.dirX = 0
        self.dirY = 0
        self.death_count = 0
        self.image = load_image('resource/png/pacman.png')



    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw_bb(self):
        draw_rectangle(*self.get_bb())





class item:
    image = None

    def __init__(self, x, y, num):
        self.x, self.y = x, y
        self.type = num
        if item.image == None:
            item.image = load_image('resource/png/item.png')

    def draw(self):
        self.image.clip_draw(int(self.type / 4)*40, (self.type %4)* 40, 40, 40, self.x, self.y)


    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def draw_bb(self):
        draw_rectangle(*self.get_bb())