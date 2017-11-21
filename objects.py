from pico2d import*

#d
class Player:

    PIXEL_PER_METER = (30.0 / 1.0)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 3.5  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 5

    image = None

    RIGHT, LEFT, UP, DOWN = 3, 2, 1, 0

    def __init__(self):
        self.x, self.y = 30, 30
        self.frame = 0
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dirX = 0
        self.dirY = 0
        self.state = self.RIGHT
        if Player.image == None:
            Player.image = load_image('png/pacman.png')

    def update(self, frame_time):
        self.life_time += frame_time
        distance = Player.RUN_SPEED_PPS * frame_time
        self.total_frames += Player.FRAMES_PER_ACTION * Player.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 4
        self.x += (self.dirX * distance)
        self.y += (self.dirY * distance)

    def draw(self):
        self.image.clip_draw(self.frame * 30, self.state * 30, 30, 30, self.x, self.y)

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




#class item:
#    image = None

#    def __init__(self, num):
#        self.x, self.y = 0, 0
 #       self.type = num
  #      if item.image == None:
   #         Player.image = load_image('png/item.png')