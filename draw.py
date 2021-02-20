import pygame

def draw(win, color, px_per_unit, row, col, r=0):
    for i in range(row-r, row+r+1):
        for j in range(col-r, col+r+1):
            left, top = i * px_per_unit, j * px_per_unit
            pygame.draw.rect(win, color, pygame.Rect(left, top, px_per_unit, px_per_unit))