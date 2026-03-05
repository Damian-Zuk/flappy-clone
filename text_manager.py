import pygame
from graphic_engine import draw_texture, texture_text, get_font
from drawable_object import DrawableObject

pygame.font.init()

class FontManager:
    fonts = dict()

    @classmethod
    def pull_font(cls, size, font):
        font_name = font + '_' + str(size)
        if not font_name in cls.fonts:
            FontManager.initialise_font('assets/' + font + '.ttf', size, font)
        return cls.fonts.get(font + '_' + str(size))

    @classmethod
    def initialise_font(cls, font_path, size, font):
        cls.fonts[font + '_' + str(size)] = get_font(font_path, size)


class Text(DrawableObject):
    def render(self):
        draw_texture(self.texture, self.pos.x, self.pos.y)

    def set_text(self, content):
            self.texture = texture_text(FontManager.pull_font(self.size, self.font), content, self.color)
            self.width = self.texture.get_rect().width
            self.height = self.texture.get_rect().height
            self.content = content
    
    def change_text(self, content):
        if self.content != content:
            self.set_text(content)
        return self

    def __init__(self, content, x, y, size, color, z_index = 300, active = False, font = '04b19'):
        super().__init__(x, y, 0, 0, z_index, active)
        self.size = size
        self.color = color
        self.font = font
        self.set_text(str(content))
