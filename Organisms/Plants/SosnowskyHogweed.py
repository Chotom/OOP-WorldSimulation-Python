from Organisms.Plants.Plant import Plant

class SosnowskyHogweed(Plant):
    def __init__(self, posX, posY, world, strength=None):
        super().__init__(posX, posY, world, strength)
        self._strength = 10
        self._canPoison = 1

    def action(self):
        org = self._world.getOrganism(self.posX - 1, self.posY)
        if  org is not None:
            if org.canEatSosnowsky == 0 and not isinstance(org, Plant):
                self._world.setInformation(0, self, org)
                org.isAlive = 0
        
        org = self._world.getOrganism(self.posX + 1, self.posY)
        if  org is not None:
            if org.canEatSosnowsky == 0 and not isinstance(org, Plant):
                self._world.setInformation(0, self, org)
                org.isAlive = 0

        org = self._world.getOrganism(self.posX, self.posY - 1)
        if  org is not None:
            if org.canEatSosnowsky == 0 and not isinstance(org, Plant):
                self._world.setInformation(0, self, org)
                org.isAlive = 0

        org = self._world.getOrganism(self.posX, self.posY + 1)
        if  org is not None:
            if org.canEatSosnowsky == 0 and not isinstance(org, Plant):
                self._world.setInformation(0, self, org)
                org.isAlive = 0
            
        return super().action()
    

