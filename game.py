import pygame
from player_factory import PlayerFactory
from grid import Grid
from game_manager import GameManager

import os

os.environ['SDL_VIDEO_WINDOW_POS'] = '1000, 400'

surface = pygame.display.set_mode((3 * Grid.TILE_WIDTH, Grid.TOP_PANEL_HEIGHT + 3*Grid.TILE_HEIGHT))

pygame.display.set_caption('Tic Tac Toe')
pygame.font.init()
clock = pygame.time.Clock()
clock.tick(60)

game_manager = GameManager()
grid = Grid()

factory = PlayerFactory(surface)
player_one, player_two = factory.get_players()
active_player = player_one

game_over = False
valid_hit = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if not game_over and event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                tile = (pos[0] // Grid.TILE_WIDTH, (pos[1] - Grid.TOP_PANEL_HEIGHT) // Grid.TILE_HEIGHT)
                valid_hit = grid.hit(tile, active_player)
                if valid_hit:
                    game_over = game_manager.is_over(tile, grid.tiles)
                    if not game_over:
                        if active_player == player_one:
                            active_player = player_two
                        else:
                            active_player = player_one

    surface.fill((0, 0, 0))
    grid.draw(surface)
    game_manager.draw(surface, valid_hit, game_over, active_player)
    pygame.display.flip()
