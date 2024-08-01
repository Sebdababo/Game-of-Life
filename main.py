import pygame
import numpy as np

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

grid = np.zeros((n_cells_x, n_cells_y))

button_width = 100
button_height = 40
start_button = pygame.Rect(width // 3 - button_width // 2, height - 45, button_width, button_height)
reset_button = pygame.Rect(2 * width // 3 - button_width // 2, height - 45, button_width, button_height)

font = pygame.font.Font(None, 36)

def update(frame):
    new_grid = grid.copy()
    for x in range(n_cells_x):
        for y in range(n_cells_y):
            n_neighbors = grid[(x-1)%n_cells_x, (y-1)%n_cells_y] + \
                          grid[(x)%n_cells_x, (y-1)%n_cells_y] + \
                          grid[(x+1)%n_cells_x, (y-1)%n_cells_y] + \
                          grid[(x-1)%n_cells_x, (y)%n_cells_y] + \
                          grid[(x+1)%n_cells_x, (y)%n_cells_y] + \
                          grid[(x-1)%n_cells_x, (y+1)%n_cells_y] + \
                          grid[(x)%n_cells_x, (y+1)%n_cells_y] + \
                          grid[(x+1)%n_cells_x, (y+1)%n_cells_y]
            
            if grid[x, y] == 1:
                if n_neighbors < 2 or n_neighbors > 3:
                    new_grid[x, y] = 0
            else:
                if n_neighbors == 3:
                    new_grid[x, y] = 1
    return new_grid

running = True
simulating = False
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if y < height - 50:
                grid[x // cell_size, y // cell_size] = 1
            elif start_button.collidepoint(event.pos):
                simulating = not simulating
            elif reset_button.collidepoint(event.pos):
                grid = np.zeros((n_cells_x, n_cells_y))
                simulating = False

    screen.fill(BLACK)

    for x in range(n_cells_x):
        for y in range(n_cells_y):
            if grid[x, y] == 1:
                pygame.draw.rect(screen, WHITE, (x*cell_size, y*cell_size, cell_size-1, cell_size-1))

    pygame.draw.rect(screen, GREEN if simulating else RED, start_button)
    pygame.draw.rect(screen, GRAY, reset_button)
    
    start_text = font.render("Stop" if simulating else "Start", True, BLACK)
    reset_text = font.render("Reset", True, BLACK)
    screen.blit(start_text, (start_button.x + 20, start_button.y + 10))
    screen.blit(reset_text, (reset_button.x + 20, reset_button.y + 10))

    if simulating:
        grid = update(grid)

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
