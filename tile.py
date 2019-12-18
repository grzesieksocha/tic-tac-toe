class Tile:
    def __init__(self, pos):
        self.pos = pos
        self.sign = None

    def hit(self, sign):
        self.sign = sign
