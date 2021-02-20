import numpy as np
import pygame
from Grid import Grid
from draw import draw
from Model import Model

def main(w, h, rows, cols):
    pygame.init()

    grid = Grid(rows, cols)
    px_per_unit = w // rows

    win = pygame.display.set_mode([w, h])
    mod = Model()

    running = True
    while running:
        x, y = pygame.mouse.get_pos()
        row, col = grid.get_coords(x, y, w, h)

        if pygame.mouse.get_pressed()[0]:
            grid.paint(row, col)
            white = (255,255,255)
            draw(win, white, px_per_unit, row, col)

        if pygame.mouse.get_pressed()[2]:
            grid.erase(row, col)
            black = (0,0,0)
            draw(win, black, px_per_unit, row, col, r=1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.mod and pygame.K_KP_ENTER:
                    grid_data = np.array([np.transpose(np.array(grid.repr)).reshape(rows**2,)])
                    prediction = mod.get_most_likely(grid_data)
                    print(prediction)

        #win.fill((255,255,255))
        pygame.display.flip()

if __name__ == '__main__':
    WIDTH, HEIGHT, ROWS, COLS = 500, 500, 28, 28
    main(WIDTH, HEIGHT, ROWS, COLS)