import pygame

pygame.init()

swidth = 504
sheight = 896

screen = pygame.display.set_mode((swidth, sheight))
clock = pygame.time.Clock()

scale_x = 1.0
scale_y = 1.0

is_running = True
frame_time = 0.0
fps_cap = 100   

def get_texture(path, w, h):
    return pygame.transform.scale(pygame.image.load(path), (int(w * scale_x), int(h * scale_y)))

def draw_texture(texture, x, y):
    screen.blit(texture, (int(x * scale_x), int(y * scale_y)))

def draw_rect(x, y, w, h, color):
    pygame.draw.rect(screen, color, (int(x * scale_x), int(y * scale_y), int(w * scale_x), int(h * scale_y)))

def texture_text(font, content, color):
    return font.render(content, False, color)

def get_font(font_path, size):
    return pygame.font.Font(font_path, int(size))

def update_display():
    pygame.display.update()

def collision_aabb(x1, y1, w1, h1, x2, y2, w2, h2):
    return x1 + w1 > x2 and x1 < x2 + w2 and y1 + h1 > y2 and y1 < y2 + h2