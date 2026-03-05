from drawable_object import DrawableObject
from event_handler import EventHandler
from graphic_engine import collision_aabb

class Button(DrawableObject):
    wait_for_release = False

    def update(self):
        if EventHandler.tap > 0 and not self.wait_for_release:
            if collision_aabb(self.pos.x, self.pos.y, self.width, self.height, EventHandler.pos.x, EventHandler.pos.y, 1, 1):
                self.texture = self.hold_texture
                self.wait_for_release = True
        elif EventHandler.tap == 0 and self.wait_for_release:
            self.texture = self.normal_texture
            self.wait_for_release = False
            if collision_aabb(self.pos.x, self.pos.y, self.width, self.height, EventHandler.pos.x, EventHandler.pos.y, 1, 1):
                self.on_click()



    def __init__(self, img_path, img_hold_path, on_click, x, y, w, h, z_index = 400, active = False):
        super().__init__(x, y, w, h, z_index, active)
        self.normal_texture = self.load_texture(img_path, False)
        self.hold_texture = self.load_texture(img_hold_path, False)
        self.texture = self.normal_texture
        self.has_texture = True
        self.on_click = on_click