from Organisms.Animals.Animal import Animal
import random

class Antelope(Animal):
     def __init__(self, posX, posY, world, strength=None):
        super().__init__(posX, posY, world, strength)
        self._initiative = 4
        self._canEscape = 1
        if strength is not None:
            self._strength = strength
        else:
            self._strength = 4

     def action(self):
        walkBoostChange = random.randint(0, 1)
        if walkBoostChange == 1:
            self._walkBoost = 1
        else:
            self._walkBoost = 0
        return super().action()