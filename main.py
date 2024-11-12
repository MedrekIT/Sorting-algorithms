import pygame as pg
from sorting import SortingAnimation as SAni
from sorting import SortingAlgorithms as SAlg

pg.init()

WIN = pg.display.set_mode((1400, 800))
pg.display.set_caption("Sorting algorithms")

if __name__ == '__main__':
    runWin = True
    clock = pg.time.Clock()

    t = [0] * 300

    SAlg.randomize(t, len(t))

    while runWin:
        clock.tick(60)
        WIN.fill((0, 0, 0))

        SAni.writeinfo(WIN, t)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                runWin = False
            if event.type != pg.KEYDOWN:
                continue
            if event.key == pg.K_b:
                SAlg.bubblesort(WIN, t)
            if event.key == pg.K_d:
                SAni.draw(WIN, t, len(t))
            if event.key == pg.K_i:
                SAlg.insertionsort(WIN, t)
            if event.key == pg.K_q:
                SAlg.quicksort(WIN, t, 0, len(t) - 1)
            if event.key == pg.K_s:
                SAlg.selectionsort(WIN, t)
            if event.key == pg.K_r:
                SAlg.randomize(t, len(t))
            if event.key == pg.K_h:
                SAlg.heapsort(WIN, t, len(t))

    pg.quit()
