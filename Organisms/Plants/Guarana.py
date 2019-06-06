from Organisms.Plants.Plant import Plant

class Guarana(Plant):
    def __init__(self, posX, posY, world, strength=None):
        super().__init__(posX, posY, world, strength)
        self._boost = 3

