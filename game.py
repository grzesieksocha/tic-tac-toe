import pygame
from player_factory import PlayerFactory
from grid import Grid
from game_state import GameState
from game_manager import is_over, switch_player

import os

os.environ['SDL_VIDEO_WINDOW_POS'] = '1000, 400'

surface = pygame.display.set_mode((600, 700))

pygame.display.set_caption('Tic Tac Toe')
pygame.font.init()
clock = pygame.time.Clock()
clock.tick(60)

game_state = GameState()
grid = Grid(game_state)

factory = PlayerFactory(surface)
player_one, player_two = factory.get_players()

game_over = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if not game_over and event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                tile = (pos[0] // 200, (pos[1] - 100) // 200)
                valid_hit = grid.hit(tile)
                if valid_hit:
                    game_over = is_over(tile, grid.tiles)

                if game_over:
                    game_state.set_player(f'{game_state.weapon} WINS!')

                if valid_hit and not game_over:
                    switch_player(game_state)

    surface.fill((0, 0, 0))
    grid.draw(surface)
    game_state.draw(surface)
    pygame.display.flip()
