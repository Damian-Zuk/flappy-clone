import graphic_engine

from vector2d import *
from operator import attrgetter
from game_object import GameObject
from resource_manager import ResourceManager


class DrawableObject(GameObject):
    def load_texture(self, path, to_main_texture = True):
        if to_main_texture:
            self.texture = graphic_engine.get_texture(path, self.width, self.height)
            self.has_texture = True
        else:
            return graphic_engine.get_texture(path, self.width, self.height)

    def render(self):
        if self.has_texture:
            graphic_engine.draw_texture(self.texture, self.pos.x, self.pos.y)
        else:
            graphic_engine.draw_rect(self.pos.x, self.pos.y, self.width, self.height, self.draw_color)        

    def center(self):
        self.pos.x = (graphic_engine.swidth - self.width) >> 1
        return self

    def __init__(self, x, y, w, h, z_index = 0, active = True, color = (0, 0, 0)):
        super().__init__(active)
        self.pos = Vector2D(x, y)
        self.width = w
        self.height = h
        self.draw_color = color
        self.has_texture = False
        self.z_index = z_index
        ResourceManager.drawable_objects.append(self)
        ResourceManager.drawable_objects.sort(key=attrgetter('z_index'))

    def delete(self):
        ResourceManager.drawable_objects.remove(self)
        super().delete()
        