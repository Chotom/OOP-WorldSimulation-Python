from tkinter.filedialog import *
import random
from Organisms import Organism
from Organisms.Animals.Wolf import Wolf
from Organisms.Animals.Antelope import Antelope
from Organisms.Animals.Fox import Fox
from Organisms.Animals.Sheep import Sheep
from Organisms.Animals.CyberSheep import CyberSheep
from Organisms.Animals.Turtle import Turtle
from Organisms.Animals.Human import Human

from Organisms.Plants.Grass import Grass
from Organisms.Plants.Dandelion import Dandelion
from Organisms.Plants.DeadlyNightshade import DeadlyNightshade
from Organisms.Plants.Guarana import Guarana
from Organisms.Plants.SosnowskyHogweed import SosnowskyHogweed


class World(object):
    def __init__(self, worldWindow, sizeX, sizeY, worldInfo):
        self.__worldWindow = worldWindow
        self.__sizeX = sizeX
        self.__sizeY = sizeY
        self._worldInfo = worldInfo
        self.__turn = 0
        self.__information = 0
        self.__boost = 0
        self.__initiativeList = []
        self.__humanAlive = 0;
        self.__messageInfo = ""
        self.__humanZn = ""
        self.__ORGANISMS = [Wolf, Antelope, Fox, Sheep, Turtle, Grass, Dandelion, DeadlyNightshade, Guarana, SosnowskyHogweed, CyberSheep]

        self.__addHuman()


    # Every organism make action and children become adults at the end of turn
    def setNextTurn(self):
        self.__messageInfo = ""
        self.__turn+=1
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
        self.__worldWindow.delete("all")
        self.drawWorld()

        self._worldInfo.set(self.__messageInfo)

    # Draw world and calculate size of single tile
    def drawWorld(self):
        width = int(self.__worldWindow.cget("width"))
        height = int(self.__worldWindow.cget("height"))
        if self.sizeX > self.sizeY: 
          self._tileWidth = width / self.__sizeX
        else:
          self._tileWidth = height / self.__sizeY

        for i in range(self.__sizeX):
            for j in range(self.__sizeY):
                x0 = (j * self._tileWidth)
                y0 = (i * self._tileWidth)
                self.__worldWindow.create_rectangle(x0, y0, x0 + self._tileWidth, y0 + self._tileWidth, fill="white")

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
            self.__worldWindow.create_rectangle(x*self._tileWidth, y*self._tileWidth, x*self._tileWidth + self._tileWidth, y*self._tileWidth + self._tileWidth, fill="white")
            return

        for Organism in self.__ORGANISMS:
            if nameOfOrg == Organism.__name__:
                if y < self.sizeX and x < self.sizeY:
                    newOrg = Organism(x, y, self)
                    self.addOrganism(newOrg)
                    if self.__turn != 0:
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

    # Delete all dead organisms from list                    
    def deleteOrganism (self):
        self.__initiativeList = [org for org in self.__initiativeList if org.isAlive]
        self.__humanAlive = 0
        for org in self.__initiativeList:
           if isinstance(org, Human):
              self.__humanAlive = 1

    # Return nearest Sosnowsky Hogweed of given coords
    def getNearestSosnowsky(self, posX, posY):
        nearestSosonowsky = None
        minX = self.__sizeX
        minY = self.__sizeY
        for sosn in self.__initiativeList:
            if isinstance(sosn, SosnowskyHogweed) and sosn.isAlive == 1:
                if abs(sosn.posX - posX) + abs(sosn.posY - posY) < minX + minY:
                    minX = abs(sosn.posX - posX)
                    minY = abs(sosn.posY - posY)
                    nearestSosonowsky = sosn
        
        return nearestSosonowsky

    # Add human to random possition
    def __addHuman(self):
        x = random.randint(0, self.sizeY - 1)
        y = random.randint(0, self.sizeX - 1)
        if self.__humanAlive == 0:
            self.addOrganism(Human(x, y, self))
            self.__humanAlive = 1
    
    # Delete List and reset variables
    def __clear(self):
        self.deleteOrganism()
        self. __initiativeList.clear()
        self.__worldWindow.delete("all")
        self.__humanAlive = 0
 
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
        #5 - human use superability
        if i == 5:
            self.__messageInfo += org.__class__.__name__ + "(" + str(org.posX) + "," + str(org.posY) + ")" + " used antelope speed" + "\n"
        #6 - human lost his turn
        if i == 6:
            self.__messageInfo += org.__class__.__name__ + "(" + str(org.posX) + "," + str(org.posY) + ")" + " already used his superability" + "\n"

    # Recreate world with new size
    def changeSize(self, sizeX, sizeY):
        self.__clear()
        if sizeX > 50:
            sizeX = 50
        if sizeY > 50:
            sizeY = 50
       
        self.__sizeX = sizeX
        self.__sizeY = sizeY
        self.__turn = 0
        self.__information = 0
        self.__boost = 0
        self.__initiativeList = []
        self.__humanAlive = 0;
        self.__messageInfo = ""
        self.__addHuman()
        self.__worldWindow.delete("all")
        self.drawWorld()
    
    # Save organisms to file
    def saveToFile(self):
        file = asksaveasfile()
        file.write(str(self.sizeX) + "\n")
        file.write(str(self.sizeY) + "\n")
        file.write(str(self.__turn) + "\n")
        for org in self.__initiativeList:
            file.write(org.getOrgToSave())
        file.close()

    # Load organism from file
    def loadFile(self):
        file = askopenfile()
        self.changeSize(int(file.readline()), int(file.readline()))
        self.__turn = int(file.readline())
        self.__clear()

        for lineOrg in file:
            orgList = lineOrg.split(" ")
            for Organism in self.__ORGANISMS:
                if orgList[0] == Organism.__name__:
                    newOrg = Organism(int(orgList[1]), int(orgList[2]), self, int(orgList[3]))
                    self.addOrganism(newOrg)
                    if self.__turn != 0:
                        newOrg.canReproduce=1
                        newOrg.isBorn=0
                    newOrg.draw(self._tileWidth)
                    break;
                elif orgList[0] == "Human":
                    newOrg = Human(int(orgList[1]), int(orgList[2]), self, int(orgList[3]), int(orgList[4]))
                    self.addOrganism(newOrg)
                    self.__humanAlive = 1
                    if self.__turn != 0:
                        newOrg.canReproduce=1
                        newOrg.isBorn=0
                    newOrg.draw(self._tileWidth)
                    break;

        file.close()
        self.drawWorld()

    # Set human action
    def setHumanZn(self, zn):
        self.__humanZn = zn
        if self.__humanAlive == 1:
            self.setNextTurn()

    # Getters
    @property
    def worldWindow(self):
        return self.__worldWindow
    @property
    def sizeX(self):
        return self.__sizeX
    @property
    def sizeY(self):
        return self.__sizeY
    @property
    def information(self):
        return self.__information
    @property
    def humanZn(self):
        return self.__humanZn

    
