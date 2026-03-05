import graphic_engine
import os
import psutil
import loader

from settings import Settings
from bird import Bird
from flappy import Flappy
from debug_info import DebugInfo
from event_handler import EventHandler
from resource_manager import ResourceManager
from scene_manager import SceneManager

DEBUG = False

class Game:
    def setup(self):
        loader.load()
        self.bird = Bird()
        Flappy.reset_game(self.bird)
        self.process = psutil.Process(os.getpid())
        
    def update(self):
        Flappy.update()
        for obj in ResourceManager.game_objects:
            if obj.active:
                obj.update()

        # Print variables
        if DEBUG and graphic_engine.frame_time > 0:
            DebugInfo.print_info(int(1 / graphic_engine.frame_time), 'fps')
            DebugInfo.print_info(graphic_engine.frame_time, 'frametime')
            DebugInfo.print_info('{} KB'.format(int(self.process.memory_info().rss / 1024)), 'MEMORY USAGE')
            DebugInfo.print_info(str(len(Flappy.pipes)), 'PIPES')
            DebugInfo.update()

    def render(self):
        graphic_engine.screen.fill((9, 87, 97))
        for obj in ResourceManager.drawable_objects:
            if obj.active:
                obj.render()

    def __init__(self):
        self.setup()

    def __del__(self):
       ResourceManager.cleanup()
            