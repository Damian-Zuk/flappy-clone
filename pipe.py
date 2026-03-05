import graphic_engine
from drawable_object import DrawableObject

class Pipe(DrawableObject):
    def render(self):
        super().render()
        if self.type == 0:
            graphic_engine.draw_rect(self.pos.x - 5, self.height - 40, self.width + 10, 40, (15, 140, 3))
        else:
            graphic_engine.draw_rect(self.pos.x - 5, self.pos.y, self.width + 10, 40, (15, 140, 3)) 

    def __init__(self, x, y, w, h, _type, z_index = 30, active = True):
        super().__init__(x, y, w, h, z_index, active)
        self.draw_color = (32, 160, 3)
        self.type = _type
