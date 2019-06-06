from Organisms.Animals.Animal import Animal
import random

class Human(Animal):
    def __init__(self, posX, posY, world, strength=None, cooldown=None):
        super().__init__(posX, posY, world, strength)
        self._initiative = 4
        if strength is not None:
            self._strength = strength
        else:
            self._strength = 5
        if cooldown is not None:
            self._cooldown = cooldown
        else:
            self._cooldown = 0
        
    # Make action as Human
    def action(self):
        walkRange = 1
        changeX = 0
        changeY = 0
        zn = self._world.humanZn

        # Set super ability
        if self._cooldown > 7:
            self._walkBoost = 1
        
        elif self._cooldown > 5:
            walkBoostChange = random.randint(0, 1)
            if walkBoostChange == 1:
                self._walkBoost = 1
            else:
                self._walkBoost = 0

        if self._walkBoost == 1:
            walkRange = 2     
        self._walkBoost = 0

        if self._cooldown > 0:
           self._cooldown-=1

        if zn == "r":
            if self._cooldown == 0:
                self._cooldown = 10
                self._world.setInformation(5, self, None)
            else:
                self._world.setInformation(6, self, None)
        # Walking
        else:
            if zn == "w":
                changeX -= walkRange
                if changeX + self.posX < 0: 
                    changeX = 0
            elif zn == "s":
                changeX += walkRange
                if changeX + self.posX >= self._world.sizeY: 
                    changeX = 0
            elif zn == "a":
                changeY -= walkRange
                if changeY + self.posY < 0: 
                    changeY = 0
            elif zn == "d":
                changeY += walkRange
                if changeY + self.posY >= self._world.sizeX:                    
                    changeY = 0
        
        if changeX != 0 or changeY != 0:
            enemy = self._world.getOrganism(self.posX + changeX, self.posY + changeY)

            if enemy is not None:
                return enemy.collision(self, changeX, changeY)
            else:
                self.posX += changeX
                self.posY += changeY

    # Return string to save human with cooldown
    def getOrgToSave(self):
        return self.__class__.__name__ + " " + str(self.posX) + " " + str(self.posY) + " " + str(self.strength) + " " + str(self._cooldown) +"\n"



