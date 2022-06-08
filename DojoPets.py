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



class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        print(f"{self.first_name} is walking {self.pet.name}!")

    def feed(self):
        self.pet.eat()
        print(f"{self.first_name} is feeding {self.pet.name} {self.pet_food}!")

    def bathe(self):
        self.pet.noise("chirp chirp!")
        print(f"{self.first_name} is bathing {self.pet.name}!")



mary = Ninja("Mary", "Joseph", "sugar", "seeds", Pet("Mr. Chirps", "parakeet", "flies", 50, 10))

mary.feed()
mary.walk()
mary.bathe()

# Use Inheritance to create sub classes of pets

class BigPet(Pet):
    def __init__(self, name, type, tricks, energy, health, weight):
        super().__init__(name, type, tricks, energy, health)
        self.weight = weight

    def weight_msg(self):
        if self.weight > 100:
            print("Whoa, that's a big pet!")

jackie = Ninja("Jackie", "Arnold", "Pupperoni", "Blue Buffalo", BigPet("Checkers", "dog", "rolls around", 100, 100, 150))

jackie.feed()
jackie.pet.weight_msg()

class ScalyPet(Pet):
    def __init__(self, name, type, tricks, energy, health, has_scales):
        super().__init__(name, type, tricks, energy, health)
        self.has_scales = has_scales

    def scales_msg(self):
        if self.has_scales == True:
            print("That pet sure has scales!")

gary = Ninja("Gary", "Beavers", "Pellets", "fish food", ScalyPet("Pepper", "fish", "swims", 10, 10, True))

gary.feed()
gary.pet.scales_msg()