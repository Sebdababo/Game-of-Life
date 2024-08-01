import pygame
import numpy as np
import time

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("SebDaBaBo's Game of Life")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

cell_size = 10

n_cells_x = width // cell_size
n_cells_y = (height - 50) // cell_size

grid = np.zeros((n_cells_x, n_cells_y), dtype=np.int8)

button_width = 100
button_height = 40
button_radius = 10
start_button = pygame.Rect(width // 3 - button_width // 2, height - 45, button_width, button_height)
reset_button = pygame.Rect(2 * width // 3 - button_width // 2, height - 45, button_width, button_height)

font = pygame.font.Font(None, 36)

def draw_rounded_rect(surface, rect, color, corner_radius):
    pygame.draw.rect(surface, color, rect.inflate(-2*corner_radius, 0))
    pygame.draw.rect(surface, color, rect.inflate(0, -2*corner_radius))
    pygame.draw.circle(surface, color, (rect.left+corner_radius, rect.top+corner_radius), corner_radius)
    pygame.draw.circle(surface, color, (rect.right-corner_radius, rect.top+corner_radius), corner_radius)
    pygame.draw.circle(surface, color, (rect.left+corner_radius, rect.bottom-corner_radius), corner_radius)
    pygame.draw.circle(surface, color, (rect.right-corner_radius, rect.bottom-corner_radius), corner_radius)

def update(grid):
    neighbors = np.zeros((n_cells_x, n_cells_y), dtype=np.int8)
    neighbors[1:, 1:] += grid[:-1, :-1]
    neighbors[1:, :-1] += grid[:-1, 1:]
    neighbors[:-1, 1:] += grid[1:, :-1]
    neighbors[:-1, :-1] += grid[1:, 1:]
    neighbors[:-1, :] += grid[1:, :]
    neighbors[1:, :] += grid[:-1, :]
    neighbors[:, :-1] += grid[:, 1:]
    neighbors[:, 1:] += grid[:, :-1]
    
    return ((neighbors == 3) | ((grid == 1) & (neighbors == 2))).astype(np.int8)

def draw_line(start, end, action):
    x0, y0 = start
    x1, y1 = end
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    while True:
        cell_x, cell_y = x0 // cell_size, y0 // cell_size
        if 0 <= cell_x < n_cells_x and 0 <= cell_y < n_cells_y:
            grid[cell_x, cell_y] = action

        if x0 == x1 and y0 == y1:
            break

        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy

running = True
simulating = False
drawing = False
erasing = False
last_pos = None
clock = pygame.time.Clock()

update_interval = 0.1
last_update = time.time()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos
                if y < height - 50:
                    drawing = True
                    last_pos = x, y
                    grid[x // cell_size, y // cell_size] = 1
                elif start_button.collidepoint(event.pos):
                    simulating = not simulating
                elif reset_button.collidepoint(event.pos):
                    grid.fill(0)
                    simulating = False
            elif event.button == 3:
                x, y = event.pos
                if y < height - 50:
                    erasing = True
                    last_pos = x, y
                    grid[x // cell_size, y // cell_size] = 0
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
            elif event.button == 3:
                erasing = False
            last_pos = None
        elif event.type == pygame.MOUSEMOTION:
            if drawing or erasing:
                x, y = event.pos
                if y < height - 50:
                    if last_pos:
                        draw_line(last_pos, (x, y), 1 if drawing else 0)
                    last_pos = x, y

    screen.fill(BLACK)

    for x in range(n_cells_x):
        for y in range(n_cells_y):
            if grid[x, y] == 1:
                pygame.draw.rect(screen, WHITE, (x*cell_size, y*cell_size, cell_size-1, cell_size-1))

    draw_rounded_rect(screen, start_button, GREEN if simulating else RED, button_radius)
    draw_rounded_rect(screen, reset_button, GRAY, button_radius)
    
    start_text = font.render("Stop" if simulating else "Start", True, BLACK)
    reset_text = font.render("Reset", True, BLACK)
    screen.blit(start_text, (start_button.x + 20, start_button.y + 10))
    screen.blit(reset_text, (reset_button.x + 20, reset_button.y + 10))

    current_time = time.time()
    if simulating and current_time - last_update >= update_interval:
        grid = update(grid)
        last_update = current_time

    pygame.display.flip()
    clock.tick(60)

pygame.quit()