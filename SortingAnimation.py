import pygame as pg

def draw(win, t, size, col=None, sorting=False):
    if col is None:
        col = {}
    pg.draw.rect(win, (0, 0, 0), (0, 0, 1400, 800))
    for i in range(size):
        if i in col:
            color = col[i]
        else:
            color = (0, 255, 0)
        pg.draw.lines(win, color, True,
                      [((i * 1400 + 700) // size, 700), ((i * 1400 + 700) // size, 700 - (700 / size) * t[i])], 1400 // (2 * size))
    if sorting:
        pg.display.update()

def writeinfo(win, t):
    pg.draw.circle(win, (0, 0, 255), (400, 400), 50, 5)
    draw(win, t, len(t))
    pg.display.update()