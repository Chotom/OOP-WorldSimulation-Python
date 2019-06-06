from Organisms.Animals.Animal import Animal
import random

class Turtle(Animal):
    def __init__(self, posX, posY, world, strength=None):
        super().__init__(posX, posY, world, strength)
        self._initiative = 1 
        if strength is not None:
            self._strength = strength
        else:
            self._strength = 2
    
    # 25% chance to move
    def action(self):
        canMove = random.randint(0, 4)
        if canMove == 0: 
            return super().action();
        else:
            return 0;

