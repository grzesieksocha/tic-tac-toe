import pygame
import os
from game_manager import switch_player
from tile import Tile

weapon_x = pygame.image.load(os.path.join('images', 'x.png'))
weapon_o = pygame.image.load(os.path.join('images', 'o.png'))


class Grid:
    """
    Grid lines and tiles.
    """

    def __init__(self, game_state):
        self.game_state = game_state
        self.grid_lines = [((0, 100), (600, 100)),
                           ((0, 300), (600, 300)),
                           ((0, 500), (600, 500)),
                           ((200, 100), (200, 700)),
                           ((400, 100), (400, 700))]

        self.tiles = {(x, y): Tile((x, y)) for x in range(3) for y in range(3)}

    def draw(self, surface):
        for line in self.grid_lines:
            pygame.draw.line(surface, (200, 200, 200), line[0], line[1], 2)

        for y in range(3):
            for x in range(3):
                sign = self.tiles[(x, y)].sign
                if sign == 'X':
                    surface.blit(weapon_x, (5 + x * 200, 105 + y * 200))
                elif sign == 'O':
                    surface.blit(weapon_o, (5 + x * 200, 105 + y * 200))

    def hit(self, tile):
        if not self.tiles[tile].sign:
            self.tiles[tile].hit(self.game_state.weapon)
            switch_player(self.game_state)
        else:
            self.game_state.set_player('Invalid move!')
