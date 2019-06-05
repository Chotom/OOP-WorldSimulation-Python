from Organisms.Animals.Animal import Animal

class Sheep(Animal):
        super().__init__(posX, posY, world, strength)
        self._initiative = 5 
        if strength is not None:
            self._strength = strength
        else:
            self._strength = 8


