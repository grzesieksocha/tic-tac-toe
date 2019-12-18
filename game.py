import pygame
from grid import Grid
from game_state import GameState
from game_manager import is_over

import os

os.environ['SDL_VIDEO_WINDOW_POS'] = '1000, 400'

surface = pygame.display.set_mode((600, 700))

pygame.display.set_caption('Tic Tac Toe')

game_state = GameState()
grid = Grid(game_state)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                tile = (pos[0] // 200, (pos[1] - 100) // 200)
                grid.hit(tile)

        if is_over(grid.tiles):
            game_state.set_player('.... WINS!')

    surface.fill((0, 0, 0))
    grid.draw(surface)
    game_state.draw(surface)

    pygame.display.flip()
