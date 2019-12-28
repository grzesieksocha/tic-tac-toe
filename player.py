from weapon import Weapon


class Player:
    def __init__(self, name: str, weapon: Weapon):
        self.weapon = weapon
        self.name = name
