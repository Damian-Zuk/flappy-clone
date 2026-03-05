import time
import graphic_engine
import math
import random

from highscore import *
from event_handler import EventHandler
from scene_manager import SceneManager
from resource_manager import ResourceManager
from settings import Settings
from pipe import Pipe
from debug_info import DebugInfo

class Flappy:
    highscore = load_highscore()
    new_best = False

    @classmethod
    def get_gap_position_offset(cls, num):
        random.seed(int(str(int(cls.game_start_time)) + str(num)))
        return random.randint(0, graphic_engine.sheight - 2 * Settings.pipe_static_part - Settings.ground_height - Settings.gap_size)

    @classmethod
    def update(cls):
        if not cls.game_over:
            if cls.distance_flew + graphic_engine.swidth  >= Settings.first_pipe:
                off = cls.distance_flew - Settings.first_pipe
                if off < 0:
                    off = 0
                first = math.floor(off / (Settings.pipe_width + Settings.spacing))
                last = first + (len(cls.pipes) >> 1)
                if first > cls.first_max:
                    cls.gap_positions.pop(0)
                    cls.gap_positions.append(cls.get_gap_position_offset(last))
                    cls.first_max = first

                for i in range(first, last):
                    x = i * (Settings.pipe_width + Settings.spacing) + Settings.first_pipe - cls.distance_flew
                    htop = Settings.pipe_static_part + cls.gap_positions[i - first]
                    ytop = 0
                    ybot = htop + Settings.gap_size
                    hbot = graphic_engine.sheight - htop - Settings.gap_size
                    p_index = i - first << 1

                    cls.pipes[p_index].pos.x = x
                    cls.pipes[p_index].pos.y = ytop
                    cls.pipes[p_index].height = htop
                    cls.pipes[p_index + 1].pos.x = x
                    cls.pipes[p_index + 1].pos.y = ybot
                    cls.pipes[p_index + 1].height = hbot

                    if graphic_engine.collision_aabb(cls.bird_instance.pos.x, cls.bird_instance.pos.y, cls.bird_instance.width, cls.bird_instance.height, x, ytop, Settings.pipe_width, htop)\
                    or graphic_engine.collision_aabb(cls.bird_instance.pos.x, cls.bird_instance.pos.y, cls.bird_instance.width, cls.bird_instance.height, x, ybot, Settings.pipe_width, hbot):
                        cls.bird_instance.die()

                    if cls.score == i:
                        if cls.bird_instance.pos.x > x + Settings.pipe_width / 2:
                            cls.score += 1
                            ResourceManager.get_res('txt_score').change_text(str(cls.score))

        if cls.game_start_time == 0:
            # Game not started yet 
            SceneManager.get_scene('died').toggle_scene(False)
            SceneManager.get_scene('died_new_best').toggle_scene(False)
            SceneManager.get_scene('tap').toggle_scene(True)
            if EventHandler.tap == 1:
                cls.start_new_game()
        else:
            # Game already started
            if cls.game_over:
                # Player died waiting for continue
                if time.time() - cls.die_time > 0.6:
                    SceneManager.get_scene('playing').toggle_scene(False)
                    if cls.new_best:
                        SceneManager.get_scene('died_new_best').toggle_scene(True)
                    else:
                        SceneManager.get_scene('died').toggle_scene(True)
            else:
                # Player currently playing
                SceneManager.get_scene('tap').toggle_scene(False)
                SceneManager.get_scene('playing').toggle_scene(True)

    @classmethod
    def start_new_game(cls):
        cls.new_best = False
        cls.gap_positions.clear()
        cls.game_start_time = time.time()
        for i in range(len(cls.pipes) >> 1):
            cls.gap_positions.append(cls.get_gap_position_offset(i))

    @classmethod
    def replay(cls):
        for pipe in cls.pipes:
            pipe.delete()
        cls.pipes.clear()
        cls.gap_positions.clear()
        cls.reset_game()

    @classmethod
    def reset_game(cls, bird_instance = None):
        cls.die_time = 0.0
        cls.game_start_time = 0.0
        cls.distance_flew = 0.0
        cls.first_max = 0
        cls.last_max = 0
        cls.score = 0
        cls.game_over = False
        cls.pipes = list()
        cls.gap_positions = list()

        for i in range(int((graphic_engine.swidth + Settings.pipe_width << 1) / (Settings.pipe_width + Settings.spacing))):
            cls.pipes.append(Pipe(graphic_engine.swidth + 100, -100, Settings.pipe_width, 1, 0))
            cls.pipes.append(Pipe(graphic_engine.swidth + 100, -100, Settings.pipe_width, 1, 1))

        ResourceManager.get_res('txt_score').change_text('0')
        if bird_instance is not None:
            cls.bird_instance = bird_instance

        cls.bird_instance.reset()
        
