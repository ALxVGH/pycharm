import pygame
import random
import math

pygame.init()
WIDTH = 600
HEIGHT = 600
field = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FPS = 20
pygame.display.set_caption('pygame')
pygame.display.update()

# Set color const
GREEN = (0, 200, 64)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


def random_color():
    c1 = random.randint(0, 255)
    c2 = random.randint(0, 255)
    c3 = random.randint(0, 255)
    colo = (c1, c2, c3)
    return colo


def mod_line_length(mod):
    global line_length
    line_length += mod


repeat = True
DIRS = [[1, 0], [0, 1], [-1, 0], [0, -1]]
radius = 20
c_trae = [300, 300]
r_trae = 100
r_trae_grow = 1
start_grad = 180
tik_grad = 5
line_length = WIDTH-radius*2
start_x = radius
start_y = WIDTH//1.2
dp = 0
ws_x = 2
wf_y = 1.1
wall_y = 100#HEIGHT // wf_y
wall_x = 200 #WIDTH // ws_x
wall_start = (wall_x, 0)
wall_end = (WIDTH, wall_y)
cross_point_x = WIDTH-((wall_y - start_y)*(WIDTH - wall_x))/wall_y
tgb = (WIDTH-wall_x)/(HEIGHT-wf_y)
cor = math.atan(tgb)
dx = radius*(1 - math.cos(cor))


def recalculate():
    global wall_start, wall_end, cross_point_x, dx
    wall_start = (wall_x, 0)
    wall_end = (WIDTH, wall_y)
    cross_point_x = WIDTH - ((wall_y - start_y) * (WIDTH - wall_x)) / wall_y
    dx = radius * (1 - math.cos(math.atan((WIDTH - wall_x) / (HEIGHT - wf_y))))


def calc_rotation_cords(pr_posx, pr_posy, ang):
    coo = [0, 0]
    coo[0] = pr_posx + math.acos(ang)
    coo[1] = pr_posy + math.asin(ang)
    return coo


# main circle:
while repeat:
    moy = 1
    mox = 1
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            repeat = False
        #while start_x+radius < cross_point_x-dx:
        field.fill(BLACK)
            #pygame.draw.line(field, GREEN, wall_start, wall_end)
            #pygame.draw.aaline(field, WHITE, (cross_point_x, 0), (cross_point_x, HEIGHT))
            #pygame.draw.line(field, WHITE, (0, start_y), (WIDTH, start_y), 1)
            #pygame.display.update()
            #grad = 5
            #rad = (grad*math.pi)/180
            #c = calc_cords(start_x, start_y, rad)
            #start_x = round(c[0])
            #start_y = round(c[1])
        x = round(math.cos(math.radians(start_grad)) * r_trae + c_trae[0])
        y = round(math.sin(math.radians(start_grad)) * r_trae + c_trae[1])
        x2 = round(math.cos(math.radians(start_grad*2)) * r_trae//2 + x)
        y2 = round(math.sin(math.radians(start_grad*2)) * r_trae//2 + y)
        x3 = round(math.cos(math.radians(start_grad * 4)) * r_trae + x2)
        y3 = round(math.sin(math.radians(start_grad * 4)) * r_trae + y2)
        pygame.draw.circle(field, RED, (x, y), radius)
        pygame.draw.circle(field, GREEN, (x, y), radius-2)
        pygame.draw.circle(field, BLUE, (x3, y3), 15)
        pygame.display.update()
        start_grad += tik_grad
        if (r_trae < 20 * radius) and (r_trae_grow == 1):
            r_trae += 1
        """elif (r_trae == 10 * radius) and (r_trae_grow == 1):
            r_trae_grow = 0
        if (r_trae > 5*radius) and (r_trae_grow ==0):
            r_trae -= 5
        elif (r_trae == 5 * radius) and (r_trae_grow == 0):
            r_trae_grow = 1"""
            #start_x += DIRS[dp][0]
            #wall_end = (WIDTH, wall_y)
            #wall_start = (wall_x, 0)
            #recalculate()
        clock.tick(FPS)
