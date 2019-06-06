from Organisms.Plants.Plant import Plant

class DeadlyNightshade(Plant):
    def __init__(self, posX, posY, world, strength=None):
        super().__init__(posX, posY, world, strength)
        self._canPoison = 1
        self._strength = 99


