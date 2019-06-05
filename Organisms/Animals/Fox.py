from Organisms.Animals.Animal import Animal
import random

class Fox(Animal):
     def __init__(self, posX, posY, world, strength=None):
        super().__init__(posX, posY, world, strength)
        self._initiative = 7
        if strength is not None:
            self._strength = strength
        else:
            self._strength = 3

     def action(self):
        possibleMove = [0, 0, 0, 0]
        freePosition = 0
        changeX = 0 
        changeY = 0

        if self.posX - 1 >= 0 and (self._world.getOrganism(self.posX - 1, self.posY) is None or self._world.getOrganism(self.posX - 1, self.posY).strength < self.strength):
            possibleMove[0] = freePosition = 1;
        if self.posX + 1 < self._world.sizeY and (self._world.getOrganism(self.posX + 1, self.posY) is None or self._world.getOrganism(self.posX + 1, self.posY).strength < self.strength):
            possibleMove[1] = freePosition = 1;
        if self.posY - 1 >= 0 and (self._world.getOrganism(self.posX, self.posY - 1) is None or self._world.getOrganism(self.posX, self.posY - 1).strength < self.strength):
            possibleMove[2] = freePosition = 1;
        if self.posY + 1 < self._world.sizeX and (self._world.getOrganism(self.posX, self.posY + 1) is None or self._world.getOrganism(self.posX, self.posY + 1).strength < self.strength):
            possibleMove[3] = freePosition = 1;

        if freePosition == 0: 
            return 0;

        while True:
            move = random.randint(0, 3)
            if possibleMove[move] == 1:
                if move == 0:
                   changeX-=1;
                elif move == 1: 
                    changeX+=1
                elif move == 2:
                    changeY-=1
                elif move == 3:
                    changeY+=1
                break
            else:
               continue
        

        enemy = self._world.getOrganism(self.posX + changeX, self.posY + changeY)
        if enemy is not None: 
            return enemy.collision(self, changeX, changeY)
        self.posX += changeX
        self.posY += changeY

        return 0
    


