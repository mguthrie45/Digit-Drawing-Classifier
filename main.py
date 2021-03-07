import numpy as np
import pygame
from Grid import Grid
from draw import draw
from Model import Model

def main(w, h, rows, cols):
    pygame.init()

    grid = Grid(rows, cols)
    px_per_unit = w // rows

    win = pygame.display.set_mode([w, h], pygame.DOUBLEBUF, 32)
    mod = Model()

    font = pygame.font.SysFont("Tahoma", 20)
    output = f'The digit you wrote is'

    running = True
    while running:
        x, y = pygame.mouse.get_pos()
        row, col = grid.get_coords(x, y, w, h)

        if pygame.mouse.get_pressed()[0]:
            grid.paint(row, col)
            white = (255,255,255)

        if pygame.mouse.get_pressed()[2]:
            grid.erase(row, col)
            black = (0,0,0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.mod and pygame.K_KP_ENTER:
                    grid_data = np.array([np.transpose(np.array(grid.repr)).reshape(rows**2,)])
                    prediction = mod.get_most_likely(grid_data)
                    output = f'The digit you wrote is {prediction}'
                    print(prediction)
        
        grid.display(win, px_per_unit)
        
        text = font.render(output, True, (255,255,255))
        win.blit(text, (120, 20))
       
        pygame.display.flip()

if __name__ == '__main__':
    WIDTH, HEIGHT, ROWS, COLS = 500, 500, 28, 28
    main(WIDTH, HEIGHT, ROWS, COLS)