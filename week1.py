class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} ate some food.")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} had a good sleep.")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} played happily!")
        else:
            print(f"{self.name} is too tired to play.")

    def train(self, trick):
        self.tricks.append(trick)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} learned a new trick: {trick}")

    def show_tricks(self):
        print(f"{self.name} knows the following tricks:")
        if self.tricks:
            for trick in self.tricks:
                print(f"- {trick}")
        else:
            print("No tricks yet.")

    def get_status(self):
        print(f"Status of {self.name}:")
        print(f"  Hunger: {self.hunger}/10")
        print(f"  Energy: {self.energy}/10")
        print(f"  Happiness: {self.happiness}/10")

# PET OBJECT with the name Fluffy:

pet = Pet("Fluffy")  

pet.get_status()
pet.eat()
pet.play()
pet.sleep()
pet.train("Sit")
pet.show_tricks()
pet.get_status()

