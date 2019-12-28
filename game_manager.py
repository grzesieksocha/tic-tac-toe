import pygame
from player import Player


class GameManager:
    @staticmethod
    def is_over(hit_tile, tiles: dict):
        def is_in_grid(x, y):
            return 0 <= x < 3 and 0 <= y < 3

        search_vectors = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        weapon = tiles[hit_tile].sign
        count = 1
        for index, (dir_x, dir_y) in enumerate(search_vectors):
            if is_in_grid(hit_tile[0] + dir_x, hit_tile[1] + dir_y) and tiles[
                    (hit_tile[0] + dir_x, hit_tile[1] + dir_y)].sign == weapon:
                count += 1
                next_x = hit_tile[0] + dir_x
                next_y = hit_tile[1] + dir_y
                if is_in_grid(next_x + dir_x, next_y + dir_y) and tiles[
                    (next_x + dir_x, next_y + dir_y)].sign == weapon:
                    count += 1
                    if count == 3:
                        return True

                if index == 0:
                    new_dir = search_vectors[1]
                elif index == 1:
                    new_dir = search_vectors[0]
                elif index == 2:
                    new_dir = search_vectors[3]
                elif index == 3:
                    new_dir = search_vectors[2]
                elif index == 4:
                    new_dir = search_vectors[5]
                elif index == 5:
                    new_dir = search_vectors[4]
                elif index == 6:
                    new_dir = search_vectors[7]
                else:
                    new_dir = search_vectors[6]

                if is_in_grid(hit_tile[0] + new_dir[0], hit_tile[1] + new_dir[1]) and tiles[
                    (hit_tile[0] + new_dir[0], hit_tile[1] + new_dir[1])].sign == weapon:
                    count += 1
                    if count == 3:
                        return True

        return False

    @staticmethod
    def draw(surface: pygame.display, is_valid_move: bool, is_game_over: bool, player: Player):
        font = pygame.font.SysFont('Arial', 30)
        if is_game_over:
            text = f'{player.name.capitalize()} won!!!'
        elif is_valid_move:
            text = player.name
        else:
            text = 'Invalid move!'

        surface.blit(font.render(text, True, (200, 200, 200)), (50, 30))
        x, y = pygame.mouse.get_pos()
        weapon = pygame.transform.scale(player.weapon.picture, (30, 30))
        surface.blit(weapon, (x + 10, y + 10))
