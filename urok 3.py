import random


class Pet:
    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type
        self.happiness = 50
        self.energy = 50
        self.hunger = 50
        self.alive = True

    def eat(self):
        print(f"{self.name} is eating ")
        self.hunger += 10
        self.happiness += 5

    def sleep(self):
        print(f"{self.name} is sleeping ")
        self.energy += 15

    def play(self):
        print(f"{self.name} is playing ")
        self.happiness += 10
        self.energy -= 5
        self.hunger -= 5

    def is_alive(self):
        if self.hunger <= 0:
            print(f"{self.name} died of hunger... ")
            self.alive = False
        elif self.happiness <= 0:
            print(f"{self.name} is depressed... ")
            self.alive = False

    def live(self, day):
        print(f"\n{self.name}: Day {day}")
        action = random.choice([self.eat, self.sleep, self.play])
        action()
        self.is_alive()


class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 100
        self.alive = True

    def to_study(self):
        print(f"{self.name} is studying ")
        self.progress += 0.12
        self.gladness -= 3

    def to_sleep(self):
        print(f"{self.name} is sleeping ")
        self.gladness += 3

    def to_chill(self):
        if self.money >= 20:
            print(f"{self.name} is having fun ")
            self.gladness += 5
            self.progress -= 0.1
            self.money -= 20
        else:
            print(f"{self.name} has no money for fun ")
            self.to_work()

    def to_work(self):
        print(f"{self.name} is working ")
        self.money += 50
        self.gladness -= 2

    def is_alive(self):
        if self.progress < -0.5:
            print(f"{self.name} has been expelled ")
            self.alive = False
        elif self.gladness <= 0:
            print(f"{self.name} has fallen into depression... ")
            self.alive = False
        elif self.progress > 5:
            print(f"{self.name} graduated early! ")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness: {self.gladness}, Progress: {round(self.progress, 2)}, Money: {self.money}")

    def live(self, day):
        print(f"\n{self.name}: Day {day}")
        if self.money < 10:
            self.to_work()
        elif self.progress < 1:
            self.to_study()
        else:
            random.choice([self.to_study, self.to_sleep, self.to_chill])()
        self.end_of_day()
        self.is_alive()


nick = Student("Nick")
kate = Student("Kate")
bohdan = Student("Bohdan")

whiskers = Pet("Whiskers", "cat")
buddy = Pet("Buddy", "dog")


for day in range(365):
    if not nick.alive or not kate.alive or not bohdan.alive:
        break
    nick.live(day)
    kate.live(day)
    bohdan.live(day)

    if whiskers.alive:
        whiskers.live(day)
    if buddy.alive:
        buddy.live(day)
