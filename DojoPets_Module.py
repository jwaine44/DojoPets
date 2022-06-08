import DojoPets_PetModule

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



mary = Ninja("Mary", "Joseph", "sugar", "seeds", DojoPets_PetModule.Pet("Mr. Chirps", "parakeet", "flies", 50, 10))

mary.feed()
mary.walk()
mary.bathe()