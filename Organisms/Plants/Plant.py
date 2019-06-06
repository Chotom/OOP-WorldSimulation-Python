from abc import ABC, abstractmethod
from Organisms.Organism import Organism
import random

class Plant(Organism, ABC):
    def __init__(self, posX, posY, world, strength=None):
        super().__init__(posX, posY, world, strength)
        self._initiative = 0
        if strength is not None:
            self._strength = strength
        else:
            self._strength = 0

    # 10% chance to reproduce
    def action(self):
        canStart = random.randint(0, 9)
        if canStart == 0:
            possiblePlant = self._tryMove(1, self.posX, self.posY);
            freePosition = 0;
            plantX = 0
            plantY = 0

            # Finding place to reproduce
            for i in range(4):
               if possiblePlant[i] == 1:
                  freePosition = 1

            if freePosition == 0:
               return 0

            while True:
                move = random.randint(0, 3)
                if possiblePlant[move] == 1:
                    if move == 0:
                       plantX-=1
                    elif move == 1:
                       plantX+=1
                    elif move == 2:
                       plantY-=1
                    elif move == 3:
                       plantY+=1
                    break
                else:
                   continue   
            # Add plant to world
            self._world.addOrganism(self.reproduce(self.posX + plantX, self.posY + plantY))
            self._world.setInformation(1, self._world.getOrganism(self.posX + plantX, self.posY + plantY), None)
        return 0
    


