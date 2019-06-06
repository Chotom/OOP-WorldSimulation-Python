from Organisms.Plants.Plant import Plant

class Dandelion(Plant):
    def __init__(self, posX, posY, world, strength=None):
        super().__init__(posX, posY, world, strength)

    def action(self):
        for i in range(3):
           super().action()
        return 0

