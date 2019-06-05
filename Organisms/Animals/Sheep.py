from Organisms.Animals.Animal import Animal

class Sheep(Animal):
      def __init__(self, posX, posY, world, strength=None):
        super().__init__(posX, posY, world, strength)
        self._initiative = 4
        if strength is not None:
            self._strength = strength
        else:
            self._strength = 4


