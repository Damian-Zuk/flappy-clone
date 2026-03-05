import time
import graphic_engine

from highscore import *
from drawable_object import DrawableObject
from settings import Settings
from event_handler import EventHandler
from resource_manager import ResourceManager
from flappy import Flappy

class Bird(DrawableObject): 
    def jump(self):
        self.falling_speed = -900.0

    def update(self):
        if Flappy.game_start_time > 0:
            if not Flappy.game_over:
                if EventHandler.tap == 1:
                    self.jump()
                if self.falling_speed < 800.0:
                    modificator = 2500.0
                    if self.falling_speed < -100.0:
                        modificator = 3500.0
                    self.falling_speed += modificator * graphic_engine.frame_time
                    if self.falling_speed > 800.0:
                        self.falling_speed = 800.0
                self.pos.y += self.falling_speed * graphic_engine.frame_time

                Flappy.distance_flew += self.flying_speed * graphic_engine.frame_time
                if self.pos.y + self.height > graphic_engine.sheight - Settings.ground_height:
                    self.die()
                    self.pos.y =  graphic_engine.sheight - Settings.ground_height - self.height
                if self.pos.y < 0:
                    self.pos.y = 0         

            else:
                if self.falling_speed < 1200.0:
                    self.falling_speed += 4000.0 * graphic_engine.frame_time
                    if self.falling_speed > 1200.0:
                        self.falling_speed = 1200.0
                self.pos.y += self.falling_speed * graphic_engine.frame_time
                if self.pos.y + self.height > graphic_engine.sheight - Settings.ground_height:
                    self.pos.y =  graphic_engine.sheight - Settings.ground_height - self.height

    def die(self):
        Flappy.game_over = True
        Flappy.die_time = time.time()
        if Flappy.score > Flappy.highscore:
            Flappy.new_best = True
            Flappy.highscore = Flappy.score
            save_highscore(Flappy.highscore)
            ResourceManager.get_res('txt_high').change_text('HIGHSCORE {}'.format(Flappy.highscore))

    def reset(self):
        self.pos.x = graphic_engine.swidth * Settings.bird_pos_x
        self.pos.y = graphic_engine.sheight * Settings.bird_pos_y
        self.flying_speed = 200.0
        self.falling_speed = 0.0

    def __init__(self):
        super().__init__(graphic_engine.swidth * Settings.bird_pos_x, graphic_engine.sheight * Settings.bird_pos_y, Settings.bird_w, Settings.bird_h, 50)
        self.flying_speed = 200.0
        self.falling_speed = 0.0
        self.load_texture('assets/bird.png')


    
