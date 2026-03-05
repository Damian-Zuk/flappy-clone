import pygame
import graphic_engine

from vector2d import *

class EventHandler:
    tap = 0
    pos = Vector2D(0, 0)

    @classmethod
    def update(cls):
        if cls.tap == 1:
            cls.tap = 2
        cls.pos.x = pygame.mouse.get_pos()[0]
        cls.pos.y = pygame.mouse.get_pos()[1]
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                graphic_engine.is_running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                cls.tap = 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                cls.tap = 1

