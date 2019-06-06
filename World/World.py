from Organisms import Organism
from Organisms.Animals.Wolf import Wolf
from Organisms.Animals.Antelope import Antelope
from Organisms.Animals.Fox import Fox
from Organisms.Animals.Sheep import Sheep
from Organisms.Animals.CyberSheep import CyberSheep
from Organisms.Animals.Turtle import Turtle

from Organisms.Plants.Grass import Grass
from Organisms.Plants.Dandelion import Dandelion
from Organisms.Plants.DeadlyNightshade import DeadlyNightshade
from Organisms.Plants.Guarana import Guarana
from Organisms.Plants.SosnowskyHogweed import SosnowskyHogweed


class World(object):
    def __init__(self, worldWindow, sizeX, sizeY, worldInfo):
        self._worldWindow = worldWindow
        self._sizeX = sizeX
        self._sizeY = sizeY
        self._worldInfo = worldInfo
        self._turn = 0
        self._information = 0
        self._boost = 0
        self.__initiativeList = []
        self.__humanAlive = 0;
        self.__messageInfo = ""
        self.ORGANISMS = [Wolf, Antelope, Fox, Sheep, Turtle, Grass, Dandelion, DeadlyNightshade, Guarana, SosnowskyHogweed, CyberSheep]

        self.addOrganism(Wolf(0, 0, self))
        self.addOrganism(Wolf(0, 1, self))

    # Every organism make action and children become adults at the end of turn
    def setNextTurn(self):
        self.__messageInfo = ""
        self._turn+=1
        for i in self.__initiativeList:
            if i.isAlive == 1:
                if i.isBorn == 1:
                    i.isBorn = 0
                elif i.canReproduce == 0:
                    1
                elif i.action():
                    i.isAlive = 0

        self.deleteOrganism()
        for i in self.__initiativeList:
            i.canReproduce = 1
            i.isBorn = 0
        self._worldWindow.delete("all")
        self.drawWorld()

        self._worldInfo.set(self.__messageInfo)

    # Draw world and calculate size of single tile
    def drawWorld(self):
        width = int(self._worldWindow.cget("width"))
        height = int(self._worldWindow.cget("height"))
        if self.sizeX > self.sizeY: 
          self._tileWidth = width / self._sizeX
        else:
          self._tileWidth = height / self._sizeY

        for i in range(self._sizeX):
            for j in range(self._sizeY):
                x0 = (j * self._tileWidth)
                y0 = (i * self._tileWidth)
                self._worldWindow.create_rectangle(x0, y0, x0 + self._tileWidth, y0 + self._tileWidth, fill="white")

        for org in self.__initiativeList:
            org.draw(self._tileWidth)

    # Add to list with coords
    def addOrganism(self, organism):
        self.__initiativeList.append(organism);
        self.__initiativeList = sorted(self.__initiativeList, key=lambda org: org.initiative, reverse=True)

    # Add choosen organism on click or remove it from tile
    def addOnClick(self, nameOfOrg, x, y):
        x = int(x/self._tileWidth)
        y = int(y/self._tileWidth)

        if self.getOrganism(x, y) is not None:
            self.getOrganism(x, y).isAlive = 0
            self.deleteOrganism()
            self._worldWindow.create_rectangle(x*self._tileWidth, y*self._tileWidth, x*self._tileWidth + self._tileWidth, y*self._tileWidth + self._tileWidth, fill="white")
            return

        for Organism in self.ORGANISMS:
            if nameOfOrg == Organism.__name__:
                if y < self.sizeX and x < self.sizeY:
                    newOrg = Organism(x, y, self)
                    self.addOrganism(newOrg)
                    if self._turn != 0:
                        newOrg.canReproduce=1
                        newOrg.isBorn=0
                    newOrg.draw(self._tileWidth)
                    return
                            

    # Return organism by his coords
    def getOrganism(self, posX, posY):
        for org in self.__initiativeList:
           if org.posX == posX and org.posY == posY and org.isAlive == 1:
               return org
        return None

    # Return nearest Sosnowsky Hogweed of given coords
    def getNearestSosnowsky(self, posX, posY):
        nearestSosonowsky = None
        minX = self._sizeX
        minY = self._sizeY
        for sosn in self.__initiativeList:
            if isinstance(sosn, SosnowskyHogweed) and sosn.isAlive == 1:
                if abs(sosn.posX - posX) + abs(sosn.posY - posY) < minX + minY:
                    minX = abs(sosn.posX - posX)
                    minY = abs(sosn.posY - posY)
                    nearestSosonowsky = sosn
        
        return nearestSosonowsky

    # Delete all dead organisms from list                      
    def deleteOrganism (self):
        self.__initiativeList = [org for org in self.__initiativeList if org.isAlive]
        #for org in self.__initiativeList:
        #   if isinsance(org, Human):
        #       __humanAlive = 0
    
    # Delete List and reset variables
    def clear(self):
        self.deleteOrganism()
        __initiativeList.clear()
        __humanAlive = 0
    
 
    def setInformation(self, i, org, enemy):
        #0 - organism killed enemy
        if i == 0:
            self.__messageInfo += org.__class__.__name__ + "(" + str(org.posX) + "," + str(org.posY) + ")" + " has killed " + enemy.__class__.__name__ + "(" + str(enemy.posX) + "," + str(enemy.posY) + ")" + "\n"
        #1 - organism is Born
        if i == 1:
            self.__messageInfo += org.__class__.__name__ + "(" + str(org.posX) + "," + str(org.posY) + ")" + " appeared " + "\n"
        #2 - organism escape
        if i == 2:
            self.__messageInfo += org.__class__.__name__ + " trying kill " + enemy.__class__.__name__ + " but " + enemy.__class__.__name__ + " escaped " + "\n"
        #3 - organism defend attack
        if i == 3:
            self.__messageInfo += org.__class__.__name__ + " trying kill " + enemy.__class__.__name__ + " but " + enemy.__class__.__name__ + " defended " + "\n"
        #4 - give boost
        if i == 4:
            self.__messageInfo += org.__class__.__name__ + "(" + str(org.posX) + "," + str(org.posY) + ")" + " give boost to " + enemy.__class__.__name__ + "\n"

    # Recreate world with new size
    def changeSize(self, sizeX, sizeY):
        self.clear
        if sizeX > 50:
            sizeX = 50
        if sizeY > 50:
            sizeY = 50
       
        self._sizeX = sizeX
        self._sizeY = sizeY
        self._turn = 0
        self._information = 0
        self._boost = 0
        self.__initiativeList = []
        self.__humanAlive = 0;
        self.__messageInfo = ""

        self._worldWindow.delete("all")
        self.drawWorld()
    
    #Getters
    @property
    def worldWindow(self):
        return self._worldWindow
    @property
    def sizeX(self):
        return self._sizeX
    @property
    def sizeY(self):
        return self._sizeY
    @property
    def information(self):
        return self._information
