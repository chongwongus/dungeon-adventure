import random

class Adventurer:
    def __init__(self, name):
        self.name = name
        self.hp = random.randint(75, 100)
        self.healingPot = 0
        self.visionPot = 0
        self.pillarsFound = []
        self.currLocation = None
        
    @property
    def hp(self):
        return self._hp
    
    @hp.getter
    def hp(self):
        return self._hp
    
    @hp.setter
    def hp(self, value):
        if value < 0:
            self._hp = 0
        elif value > 100:
            self._hp = 100
        else:
            self._hp = value
    
    @property
    def healingPot(self):
        return self._healingPot
    
    @healingPot.getter
    def healingPot(self):
        return self._healingPot
    
    @healingPot.setter
    def healingPot(self, value):
        if value < 0:
            self._healingPot = 0
        else:
            self._healingPot = value
    
    @property
    def visionPot(self):
        return self._visionPot

    @visionPot.getter
    def visionPot(self):
        return self._visionPot
    
    @visionPot.setter
    def visionPot(self, value):
        if value < 0:
            self._visionPot = 0
        else:
            self._visionPot = value

    def __str__(self):
        """
        string representation of adventurer's status
        :return:
        """
        string = (f"Adventurer: {self.name}\nHP: {self.hp}\nHealth Potions: {self.healingPot}\n"
                  f"Vision Potions: {self.visionPot}\n"
                  f"Pillars Found: {', '.join(self.pillarsFound) if self.pillarsFound else 'None'}")
        return string

    def move(self, direction):
        """
        updates current location based on direction
        :param direction:
        :return:
        """
        x, y = self.currLocation
        if direction == 'N':
            self.currLocation = (x, y - 1)
        elif direction == 'S':
            self.currLocation = (x, y + 1)
        elif direction == 'E':
            self.currLocation = (x + 1, y)
        elif direction == 'W':
            self.currLocation = (x - 1, y)

    def use_healing_pot(self):
        """
        uses healing potion if available
        :return:
        """
        if self.healingPot > 0:
            healing = random.randint(1, 100)
            self.hp += healing
            self.healingPot -= 1
            return True
        return False

    def use_vision_pot(self):
        """
        uses vision potion if available
        :return:
        """
        if self.visionPot > 0:
            self.visionPot -= 1
            return True
        return False

    def add_pillar(self, pillar):
        """
        adds pillar to collection if not already found
        :param pillar:
        :return:
        """
        if pillar not in self.pillarsFound:
            self.pillarsFound.append(pillar)

    def take_dmg(self, amount):
        """
        method for adventurer taking some amount of damage
        :param amount: damage taken
        :return:
        """
        self.hp -= amount

    def heal(self, amount):
        """
        method for adventurer healing some amount
        :param amount: healing amount
        :return:
        """
        self.hp += amount