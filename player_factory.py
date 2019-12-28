import pygame
import os
import re
from player import Player
from weapon import Weapon


class PlayerFactory:
    def __init__(self, surface):
        self.surface = surface

    def get_players(self):
        weapon_x = Weapon('X', pygame.image.load(os.path.join('images', 'x.png')))
        weapon_o = Weapon('O', pygame.image.load(os.path.join('images', 'o.png')))
        player_one = Player('Player one', weapon_x)
        player_two = Player('Player two', weapon_o)

        font = pygame.font.SysFont('Arial', 30)

        for player in [player_one, player_two]:
            input_name = ''
            during_input = True
            while during_input:
                player_text = font.render(f'{player.name} name: {input_name}', True, (200, 200, 200))
                self.surface.fill((0, 0, 0))
                self.surface.blit(player_text, (10, 10))
                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                    p = re.compile('^[a-zA-Z0-9]$')
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            during_input = False
                        elif event.key == pygame.K_BACKSPACE:
                            input_name = input_name[:-1]
                        elif p.match(event.unicode):
                            input_name += event.unicode

            player.name = input_name
        return player_one, player_two
