class Pet:
    def __init__ (self, name, type, tricks, energy, health):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = energy
        self.health = health

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        return self
    
    def noise(self, noise):
        print(noise)