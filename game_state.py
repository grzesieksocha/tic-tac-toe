import pygame

import os

weapon_x = pygame.image.load(os.path.join('images', 'x.png'))
weapon_o = pygame.image.load(os.path.join('images', 'o.png'))

weapon_x = pygame.transform.scale(weapon_x, (30, 30))
weapon_o = pygame.transform.scale(weapon_o, (30, 30))


class GameState:
    def __init__(self):
        self.player = 'Player 1'
        self.weapon = 'X'

    def set_player(self, player):
        self.player = player

    def set_weapon(self, sign):
        self.weapon = sign

    def draw(self, surface: pygame.display):
        pygame.font.init()
        font = pygame.font.SysFont('Arial', 30)

        player_text = font.render(self.player, True, (200, 200, 200))
        sign_text = font.render(self.weapon, True, (200, 200, 200))

        x, y = pygame.mouse.get_pos()
        surface.blit(player_text, (50, 30))
        if self.weapon == 'X':
            surface.blit(weapon_x, (x + 10, y + 10))
        else:
            surface.blit(weapon_o, (x + 10, y + 10))
