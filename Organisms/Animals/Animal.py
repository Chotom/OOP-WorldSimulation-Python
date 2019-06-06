from abc import ABC, abstractmethod
from Organisms.Organism import Organism
import random

class Animal(Organism, ABC):
    def __init__(self, posX, posY, world, strength=None):
        super().__init__(posX, posY, world, strength)
        self._walkBoost = 0
        if strength is not None:
            self._strength = strength
        else:
            self._strength = 1

    # Move randomly organism or call collision
    def action(self):
        if self._walkBoost:
           walkRange = 2
        else:
           walkRange = 1

        changeX = 0
        changeY = 0
        motion = random.randint(0, 3)

        
        if motion == 0:
            changeX-=walkRange
            if (changeX + self.posX) < 0: changeX *= -1
                
        elif motion == 1:
                changeX+=walkRange
                if (changeX + self.posX) >= self._world.sizeY: changeX *= -1
              
        elif motion == 2:
                changeY-=walkRange
                if (changeY + self.posY) < 0: changeY *= -1

        elif motion == 3:
                changeY+=walkRange
                if (changeY + self.posY) >= self._world.sizeX: changeY *= -1
       

        enemy = self._world.getOrganism(self.posX + changeX, self.posY + changeY)
        if enemy is not None: 
            return enemy.collision(self, changeX, changeY)
        else:
            self.posX += changeX
            self.posY += changeY

    # Create new animal when organism meet same type
    def collision(self, org, changeX, changeY):
        # Animal copulate when find type
        if isinstance(org, Animal):
            if self.__class__.__name__ == org.__class__.__name__ and self.canReproduce == 1 and org.canReproduce == 1:
                possibleBorn = self._tryMove(1, org.posX, org.posY)
                freePosition = 0
                bornX = 0
                bornY = 0
             
                for i in range(4):
                    if(possibleBorn[i] == 1): 
                        freePosition = 1

                if freePosition == 0: 
                    return 0

                while True:
                    move = random.randint(0, 3)
                    if possibleBorn[move]:
                        if move == 0:
                            bornX-=1
                        elif move == 1: 
                            bornX+=1
                        elif move == 2:
                            bornY-=1
                        elif move == 3: 
                            bornY+=1
                        break
                    else: 
                        continue
                    
                # Add baby to world and end adults turns
                self._world.addOrganism(org.reproduce((org.posX + bornX), (org.posY + bornY)))
                self._world.setInformation(1, self._world.getOrganism(org.posX + bornX, org.posY + bornY), None)
                self.canReproduce = 0
                org.canReproduce = 0
                return 0
                
            # Cant copulate with child
            elif self.__class__.__name__ == org.__class__.__name__ and (org.isBorn == 0 or self.isBorn == 0): 
                return 0
            # Adult cant copulate twice in one turn
            elif self.__class__.__name__ == org.__class__.__name__: 
                return 0
        
        return super().collision(org, changeX, changeY)
            
    

