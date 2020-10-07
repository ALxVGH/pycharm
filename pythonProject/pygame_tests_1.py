import pygame
import random
import math

pygame.init()
WIDTH = 600
HEIGHT = 600
field = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FPS = 60
gogo = True
pygame.display.set_caption('pygame')
pygame.display.update()
x = WIDTH//2
y = HEIGHT//2
path_length = 0
GREEN = (0, 200, 64)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LEFT = 3
RIGHT = 1
DOWN = 0
UP = 2
UP_R = 4
DOWN_R = 5
DOWN_L = 6
UP_L = 7
XQ = 8
RAYS = 9
RADIUS = 2
MAX_DEEP = HEIGHT-RADIUS
MAX_RIGHT = WIDTH-RADIUS
# Sq = pygame.Rect(200, 200, 70, 70)
# pygame.draw.rect(field, (255, 180, 95), (20, 100, 50, 70))
# pygame.draw.rect(field, GREEN, Sq, 2)
# pygame.draw.line(field, (255, 255, 255), (250, 300), (400, 350))
di = 0
Orientation = random.choice([1, -1])
start_angle = random.randint(1, 360)
rot_dir = random.choice([1, -1])
xc = x
yc = y
mem_x = x
mem_y = y


def random_color():
    c1 = random.randint(0, 255)
    c2 = random.randint(0, 255)
    c3 = random.randint(0, 255)
    colo = (c1, c2, c3)
    return colo


COLOR = random_color()


def ch_mem_xy():
    global mem_x, mem_y
    mem_x = x
    mem_y = y


def ch_xy():
    global x, y
    x = mem_x
    y = mem_y


def ch_cxy():
    global xc, yc
    xc = x
    yc = y


def get_direction(x_pos, y_pos):
    LD = []
    if (di != RAYS) and (di != XQ):
        LD.append(RAYS)
        ch_cxy()
    else:
        ch_xy()
    if (di != UP) and (di != DOWN):
        if y_pos > 0:
            LD.append(UP)
        if y_pos < MAX_DEEP:
            LD.append(DOWN)
    if (di != LEFT) and (di != RIGHT):
        if x_pos > 0:
            LD.append(LEFT)
        if x_pos < MAX_RIGHT:
            LD.append(RIGHT)
    if (di != UP_L) and (di != DOWN_R):
        if (x_pos > 0) and (y_pos > 0):
            LD.append(UP_L)
        if (x_pos < MAX_RIGHT) and (y_pos < MAX_DEEP):
            LD.append(DOWN_R)
    if (di != DOWN_L) and (di != UP_R):
        if (x_pos > 0) and (y_pos < MAX_DEEP):
            LD.append(DOWN_L)
        if (x < MAX_RIGHT) and (y > 0):
            LD.append(UP_R)
    if di != XQ:
        LD.append(XQ)
    '''    
    if x_pos >= MAX_RIGHT:
        direction = random.choice([UP, DOWN, LEFT, UP_L, DOWN_L])
        if y_pos >= MAX_DEEP:
            direction = random.choice([UP, LEFT, UP_L])
        if y_pos <= RADIUS:
            direction = random.choice([DOWN, LEFT, DOWN_L])
    elif x_pos <= RADIUS:
        direction = random.choice([RIGHT, UP, DOWN, UP_R, DOWN_R])
        if y_pos >= MAX_DEEP:
            direction = random.choice([UP, RIGHT, UP_R])
        if y_pos <= RADIUS:
            direction = random.choice([DOWN, RIGHT, DOWN_R])
    elif y_pos >= MAX_DEEP:
        direction = random.choice([UP, LEFT, RIGHT, UP_R, UP_L])
    elif y_pos <= RADIUS:
        direction = random.choice([DOWN, LEFT, RIGHT, DOWN_R, DOWN_L])
    else:
        direction = random.choice([UP, UP_R, RIGHT, DOWN_R, DOWN, DOWN_L, LEFT, UP_L, XQ, RAYS])
    '''
    direction = random.choice(LD)
    if direction == RAYS:
        ch_mem_xy()
    direction = 8
    return direction


def dxy(di, x, y):
    coo = [x, y]
    rand_sharp = random.randint(1, 10)
    if (di == 0) and (y < MAX_DEEP):
        coo[1] += 1
    elif (di == 1) and (x < MAX_RIGHT):
        coo[0] += 1
    elif (di == 2) and (y > RADIUS):
        coo[1] -= 1
    elif (di == 3) and (x > RADIUS):
        coo[0] -= 1
    elif (di == 4) and (y > RADIUS) and (x < MAX_RIGHT):
        coo[1] -= 1 * rand_sharp
        coo[0] += 1 * rand_sharp
    elif (di == 5) and (y < MAX_DEEP) and (x < MAX_RIGHT):
        coo[1] += 1 * rand_sharp
        coo[0] += 1 * rand_sharp
    elif (di == 6) and (y < MAX_DEEP) and (x > RADIUS):
        coo[1] += 1 * rand_sharp
        coo[0] -= 1 * rand_sharp
    elif (di == 7) and (y > RADIUS) and (x > RADIUS):
        coo[1] -= 1 * rand_sharp
        coo[0] -= 1 * rand_sharp
    elif (di == 8) and (x <= MAX_RIGHT) and (x >= RADIUS) and (y <= MAX_DEEP) and (y >= RADIUS):
        global Orientation
        #Orientation = random.choice([1, -1])
        Orientation = random.randint(-5, 5)
        coo[0] = x + 20*Orientation
        #Orientation = random.choice([1, -1])
        Orientation = random.randint(-5, 5)
        coo[1] = y + 12*Orientation
    return coo


def rxy(prev_x, prev_y, clock_direction, len_ray, prev_ang):
    coo = [0, 0]
    if clock_direction == 1:
        prev_ang = 360-prev_ang
    coo[0] = round(len_ray * math.cos(prev_ang) + prev_x)
    coo[1] = round(len_ray * math.sin(prev_ang) + prev_y)
    if coo[0] > WIDTH:
        coo[0] = WIDTH - 5
    if coo[0] <= 0:
        coo[0] = 5
    if coo[1] >= HEIGHT:
        coo[1] = HEIGHT-5
    if coo[1] <= 0:
        coo[1] = 5
    return coo


def get_rotation_coordinates(rotation_angle, rotation_radius, rotation_center):
    coordinates = [0, 0]
    coordinates[0] = round(math.cos(math.radians(rotation_angle)) * rotation_radius + rotation_center[0])
    coordinates[1] = round(math.sin(math.radians(rotation_angle)) * rotation_radius + rotation_center[1])
    return coordinates


def next_position_from_here_to_where(cur_coordinates, end_coordinates, curve_radius=0):
    coordinates = [0, 0, 0]
    if curve_radius == 0:
        if end_coordinates[0] > cur_coordinates[0]:
            coordinates[0] = cur_coordinates + 1
            coordinates[2] += 1
        elif end_coordinates[0] < cur_coordinates[0]:
            coordinates[0] = cur_coordinates -1
            coordinates[2] += 1
        if end_coordinates[1] > cur_coordinates[1]:
            coordinates[1] = cur_coordinates + 1
            coordinates[2] += 1
        elif end_coordinates[[1]] < cur_coordinates[[1]]:
            coordinates[1] = cur_coordinates - 1
            coordinates[2] += 1
    elif curve_radius > 0:
        pass
    return coordinates


while gogo:
    if path_length == 0:
        rot_dir = random.choice([1, -1])
        if di == RAYS:
            x = mem_x
            y = mem_y
        di = get_direction(x, y)
        path_length = random.randint(50, 80)
        if di == RAYS:
            path_length = random.randint(5, 15)
            COLOR = random_color()
            Orientation = random.choice([1, -1])
        start_angle = random.randint(1, 360)
    #field.fill((0, 0, 0))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            gogo = False
    if di <= 8:
        pygame.draw.circle(field, COLOR, (x, y), RADIUS, 1)
        clock.tick(FPS)
        pygame.display.set_caption('direction:' + str(di)+' p:' + str(path_length))
        pygame.display.update()
        Coords = dxy(di, x, y)
        x = Coords[0]
        y = Coords[1]
        path_length -= 1
        if (x >= MAX_RIGHT) or (x <= RADIUS) or (y >= MAX_DEEP) or (y <= RADIUS):
            path_length = random.randint(2, 300)
            di = get_direction(x, y)
            COLOR = random_color()
    elif di == 9:
        len_line = random.randint(20, 90)
        Coords = rxy(xc, yc, rot_dir, len_line, start_angle)
        x = Coords[0]
        y = Coords[1]
        pygame.draw.line(field, random_color(), (xc, yc), (x, y))
        pygame.display.update()
        path_length -= 1
        start_angle += 1
