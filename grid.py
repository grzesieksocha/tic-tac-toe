import pygame
from tile import Tile
from player import Player


class Grid:
    NUMBER_OF_TILES_ROW_COLUMN = 3
    COLOR_WHITE = (200, 200, 200)
    TOP_PANEL_HEIGHT = 80
    CLICK_OFFSET = 5
    TILE_HEIGHT = TILE_WIDTH = 200

    def __init__(self):
        self.grid_lines = [
            # Top horizontal line
            ((0, Grid.TOP_PANEL_HEIGHT), (3 * Grid.TILE_WIDTH, Grid.TOP_PANEL_HEIGHT)),
            # Middle horizontal line
            (
                (0, Grid.TOP_PANEL_HEIGHT + Grid.TILE_HEIGHT),
                (3 * Grid.TILE_WIDTH, Grid.TOP_PANEL_HEIGHT + Grid.TILE_HEIGHT)
            ),
            # Bottom horizontal line
            (
                (0, Grid.TOP_PANEL_HEIGHT + 2 * Grid.TILE_HEIGHT),
                (3 * Grid.TILE_WIDTH, Grid.TOP_PANEL_HEIGHT + 2 * Grid.TILE_HEIGHT)
            ),
            # Left vertical line
            ((Grid.TILE_WIDTH, Grid.TOP_PANEL_HEIGHT), (Grid.TILE_WIDTH, Grid.TOP_PANEL_HEIGHT + 3 * Grid.TILE_HEIGHT)),
            # Right vertical line
            (
                (2 * Grid.TILE_WIDTH, Grid.TOP_PANEL_HEIGHT),
                (2 * Grid.TILE_WIDTH, Grid.TOP_PANEL_HEIGHT + 3 * Grid.TILE_HEIGHT)
            )
        ]

        self.tiles = {(x, y): Tile((x, y))
                      for x in range(Grid.NUMBER_OF_TILES_ROW_COLUMN)
                      for y in range(Grid.NUMBER_OF_TILES_ROW_COLUMN)}

    def draw(self, surface):
        for line in self.grid_lines:
            pygame.draw.line(surface, Grid.COLOR_WHITE, line[0], line[1], 2)

        for y in range(Grid.NUMBER_OF_TILES_ROW_COLUMN):
            for x in range(Grid.NUMBER_OF_TILES_ROW_COLUMN):
                if self.tiles[(x, y)].sign is not None:
                    surface.blit(
                        self.tiles[(x, y)].sign,
                        (
                            Grid.CLICK_OFFSET + x * Grid.TILE_WIDTH,
                            Grid.TOP_PANEL_HEIGHT + Grid.CLICK_OFFSET + y * Grid.TILE_HEIGHT
                        )
                    )

    def hit(self, tile, player: Player):
        if not self.tiles[tile].sign:
            self.tiles[tile].sign = player.weapon.picture
            return True
        else:
            return False
