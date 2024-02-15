import pygame as pg
import sys
import math as m

# CONSTS
ROWS, COLS = 25, 25
dis_width, dis_height = 1200, 800
w, h = dis_width / COLS, dis_height / ROWS


class Spot:
    # all = []
    w, h = dis_width / COLS, dis_height / ROWS

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.f = 0
        self.g = 0
        self.h = 0
        self.neighbors = []
        self.previous = None
        # Spot.all.append(self)

    def __repr__(self):
        return f'Spot({self.f}, {self.g}, {self.h})'

    def show(self, color):
        rectangle = pg.Rect(self.x * Spot.w, self.y * Spot.h, Spot.w - Spot.w / 100, Spot.h - Spot.h / 100)
        pg.draw.rect(screen, color, rectangle, 0)

    def add_neighbors(self, grid):
        if self.x > 0:
            self.neighbors.append(grid[self.x - 1][self.y])
        if self.x < COLS - 1:
            self.neighbors.append(grid[self.x + 1][self.y])
        if self.y > 0:
            self.neighbors.append(grid[self.x][self.y - 1])
        if self.y < COLS - 1:
            self.neighbors.append(grid[self.x][self.y + 1])


def heuristic(start_point, end_point):
    return m.sqrt((end_point.x - start_point.x) ** 2 + (end_point.y - start_point.y) ** 2)


# Pygame initiation

pg.init()
screen = pg.display.set_mode((dis_width, dis_height))
background_color = (100, 100, 100)

# Pygame end

openSet = []
closedSet = []

# Creating a grid

grid = [[Spot(x, y) for x in range(COLS)] for y in range(ROWS)]
[[grid[x][y].add_neighbors(grid) for x in range(COLS)] for y in range(ROWS)]

start = grid[0][0]
end = grid[ROWS - 1][COLS - 1]

openSet.append(start)
path = []

#  Main loop
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    if len(openSet) > 0:
        winner = 0
        for i in range(len(openSet)):
            if openSet[i].f < openSet[winner].f:
                winner = i

        current = openSet[winner]

        if openSet[winner] == end:
            print('Found')
            # Find the path


        openSet.remove(current)
        closedSet.append(current)

        for neighbor in current.neighbors:
            if not (neighbor in closedSet):
                tempG = current.g + 1
                if neighbor in openSet:
                    if tempG < neighbor.g:
                        neighbor.g = tempG
                else:
                    neighbor.g = tempG
                    openSet.append(neighbor)
            neighbor.h = heuristic(neighbor, end)
            neighbor.f = neighbor.g + neighbor.h
            neighbor.previous = current

    screen.fill((0, 0, 0))
    [[grid[x][y].show((91, 97, 97)) for x in range(COLS)] for y in range(ROWS)]
    for i in openSet:
        i.show((0, 255, 0))

    for i in closedSet:
        i.show((255, 0, 0))

    path = []
    temp = current
    path.append(temp)
    while temp.previous:
        path.append(temp.previous)
        temp = temp.previous
    for i in path:
        i.show((0, 0, 255))

    pg.display.update()
    pg.display.flip()
