from abc import ABC, abstractmethod
from tkinter import *
from Lib import random

class Organism(ABC):
    def __init__(self, posX, posY, world, strength=None):
        self._posX = posX
        self._posY = posY
        self._world = world
        self._initiative = 0
        self._boost = 0
        self._name = "Organism"
        self._canEscape = 0
        self._canDef = 0
        self._canPoison = 0
        self._canReproduce = 0
        self._isBorn = 1
        self._isAlive = 1
        self._canEatSosnowsky = 0
        if strength is not None:
            self._strength = strength
        else:
            self._strength = 0

    @abstractmethod
    def action(self):
        return

    def reproduce(self, posX, posY):
        return self.__class__(posX, posY, self._world)

    def draw(self, tileWidth):
            self._img = PhotoImage(file="Organisms/Icons/" + self.name +".png")
            self._img = self._img.subsample(int(self._img.width()/tileWidth + 1))
            x0 = (self._posX * tileWidth)
            y0 = self._posY * tileWidth
            self._world.worldWindow.create_image(x0 + tileWidth/2, y0 + tileWidth/2, image = self._img)

    def collision(self, org, changeX, changeY):

        # Both alive nothing change
        if  self.canDef and org.strength < 5:
            self._world.setInformation(3, org, self);
            return 0
        # Give boost and def die
        elif self.boost:
            self._world.setInformation(4, org, self)
            org.strength = org.strength + self._boost

            #world.deletePosition(org)
            org.posX += changeX
            org.posY += changeY
            #world.setPosition(org)

            self.isAlive = 0

            return 0
        # Both die
        elif self.canPoison:
            #world.setInformation(0, this, org)
            #world.setInformation(0, org, this)

            self.isAlive = 0

            return 1
        

        # Defender die or escape
        elif self.strength <= org.strength:
            escape = random.randint(0, 1)
            if escape * self._canEscape == 1:
                # Check any possible way to escape and escape
                if self.__randomiseEscape(self, self.posX, self.posY):
                    self._world.setInformation(2, org, self);

                    org.posX += changeX
                    org.posY += changeY
         
                    return 0
                # Defender die
                else:
                    self._world.setInformation(0, org, self)
                    #world.deletePosition(org)
                    org.posX += changeX
                    org.posY += changeY
                    #world.setPosition(org)
                    self.isAlive = 0

                    return 0
            # Defender die
            else:
                self._world.setInformation(0, org, self);

                #world.deletePosition(org);
                org.posX += changeX;
                org.posY += changeY;
                #world.setPosition(org);
                self.isAlive = 0

                #self._world.deleteOrganism(self);
            
            return 0
        
        # Attacker die
        else: 
            self._world.setInformation(0, self, org);
            return 1
        
    
    # Return array of empty tiles
    def _tryMove(self, walkRange, posX, posY):
        possibleMove = [0, 0, 0, 0]

        if (posX - walkRange >= 0) and (self._world.getOrganism(posX - walkRange, posY) is None): 
            possibleMove[0] = 1;
        if (posX + walkRange < self._world.sizeX) and (self._world.getOrganism(posX + walkRange, posY) is None): 
            possibleMove[1] = 1;
        if (posY - walkRange >= 0) and (self._world.getOrganism(posX, posY - walkRange) is None): 
            possibleMove[2] = 1;
        if (posY + walkRange < self._world.sizeY) and (self._world.getOrganism(posX, posY + walkRange) is None): 
            possibleMove[3] = 1;
        return possibleMove;

    def __randomiseEscape(self, org, posX, posY):
        possibleMove = self._tryMove(1, posX, posY)
        freePosition = 0;

        for i in range(4): 
            if possibleMove[i]: 
                freePosition = 1
        if freePosition == 0: 
            return 0
        # Find proper way
        while True:
            changeX = 0
            changeY = 0
            move = random.randint(0, 3)
            if possibleMove[move]:
                if move == 0:
                    changeX-=1
                elif move == 1:
                    changeX+=1
                elif move == 2:
                    changeY-=1
                elif move == 3:
                    changeY+=1
                self.posX += changeX
                self.posY += changeY
                return 1
            else:
                continue


    #@isBorn.setter
    #def isBorn(self, change):
    #    self._isBorn = change

  
    #Getters ans setters
    @property
    def posX(self):
        return self._posX
    @property
    def posY(self):
        return self._posY
    @property
    def strength(self):
        return self._strength
    @property
    def initiative(self):
        return self._initiative
    @property
    def name(self):
        return self._name
    @property
    def isAlive(self):
        return self._isAlive
    @property
    def isBorn(self):
        return self._isBorn
    @property
    def canPoison(self):
        return self._canPoison
    @property
    def canReproduce(self):
        return self._canReproduce
    @property
    def canDef(self):
        return self._canDef
    @property
    def canEatSosnowsky(self):
        return self._canEatSosnowsky
    @property
    def boost(self):
        if self._boost == 0:
            return 0
        else:
            return 1

    @posX.setter
    def posX(self, X):
        self._posX = X

    @posY.setter
    def posY(self, Y):
        self._posY = Y

    @isAlive.setter
    def isAlive(self, change):
        self._isAlive = change
    @isBorn.setter
    def isBorn(self, change):
        self._isBorn = change
    
    @canReproduce.setter
    def canReproduce(self, change):
        self._canReproduce = change
    
    @strength.setter
    def strength(self, s):
        self._strength = s
