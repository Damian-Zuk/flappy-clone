import color
import graphic_engine

from resource_manager import ResourceManager
from scene_manager import SceneManager, Scene
from settings import Settings
from bird import Bird
from text_manager import Text
from button import Button
from flappy import Flappy
from drawable_object import DrawableObject


def load():
    # Resources
        ResourceManager.add_res('ground_dirt', DrawableObject(0, graphic_engine.sheight - Settings.ground_height, graphic_engine.swidth, Settings.ground_height, 31, True, (86, 64, 12)))
        ResourceManager.add_res('ground_grass', DrawableObject(0, graphic_engine.sheight - Settings.ground_height - 15, graphic_engine.swidth, 15, 32, True, (0, 163, 84)))
        ResourceManager.add_res('txt_tap', Text('TAP TO PLAY', 0, 200, 80, color.GOLD).center())
        ResourceManager.add_res('txt_over', Text('GAME OVER', 0, 200, 90, color.GOLD).center())
        ResourceManager.add_res('txt_score', Text('0', 0, 30, 96, color.WHITE).center())
        ResourceManager.add_res('txt_high', Text('HIGHSCORE {}'.format(str(Flappy.highscore)), 0, 290, 32, color.WHITE).center())
        ResourceManager.add_res('txt_best', Text('NEW BEST', 0, 140, 42, color.RED).center())
        ResourceManager.add_res('btn_replay', Button('assets/play_btn.png', 'assets/play_btn_hold.png', Flappy.replay, 0, 350, Settings.play_btn_w, Settings.play_btn_h, 250).center())
    # Scenes
        Scene('tap', 'txt_tap', 'txt_high')
        Scene('playing', 'txt_score')
        Scene('died', 'txt_score', 'txt_over', 'txt_high', 'btn_replay')
        Scene('died_new_best', 'txt_score', 'txt_best', 'txt_over', 'txt_high', 'btn_replay')