from Organisms.Animals.Sheep import Sheep

class CyberSheep(Sheep):
    def __init__(self, posX, posY, world, strength=None):
        super().__init__(posX, posY, world, strength)
        self._initiative = 4
        self._canEatSosnowsky = 1
        if strength is not None:
            self._strength = strength
        else:
            self._strength = 11

    def action(self):
        changeX = 0
        changeY = 0
        sosn = self._world.getNearestSosnowsky(self.posX, self.posY)
        if sosn is not None:
            if abs(sosn.posX - self.posX) > abs(sosn.posY - self.posY):
                changeX+= (int)((sosn.posX - self.posX) / abs(sosn.posX - self.posX))
            else:
                changeY+= (int)((sosn.posY - self.posY) / abs(sosn.posY - self.posY))

            enemy = self._world.getOrganism(self.posX + changeX, self.posY + changeY)
            if enemy is not None: 
                return enemy.collision(self, changeX, changeY)
            else:
                self.posX += changeX
                self.posY += changeY
        else:
            return super().action()

