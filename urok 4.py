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
            print(f"{self.name} ran away due to hunger... ")
            self.alive = False
        elif self.happiness <= 0:
            print(f"{self.name} is extremely sad... ")
            self.alive = False

    def live(self, day):
        print(f"\n{self.name}: Day {day}")
        action = random.choice([self.eat, self.sleep, self.play])
        action()
        self.is_alive()



class Human:
    def __init__(self, name="Human", job=None, home=None, car=None, pet=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home
        self.pet = pet

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def get_pet(self):
        pet_name = random.choice(["Buddy", "Whiskers", "Charlie", "Luna"])
        pet_type = random.choice(["dog", "cat"])
        self.pet = Pet(pet_name, pet_type)
        print(f"{self.name} adopted a pet: {self.pet.name} the {self.pet.animal_type}! 🐾")

    def care_for_pet(self):
        if self.pet and self.pet.alive:
            print(f"{self.name} is taking care of {self.pet.name} 🐕")
            action = random.choice([self.pet.eat, self.pet.play])
            action()
        elif self.pet and not self.pet.alive:
            print(f"{self.pet.name} is gone... ")

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = "fuel"
            else:
                self.to_repair()
                return
        if manage == "fuel":
            print("I bought fuel ")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print("Bought food ")
            self.money -= 50
            self.home.food += 50
        elif manage == "delicacies":
            print("Hooray! Delicious! ")
            self.gladness += 10
            self.satiety += 2
            self.money -= 15

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def days_indexes(self, day):
        day = f" Today is day {day} of {self.name}'s life "
        print(f"{day:=^50}", "\n")
        print(f"Money – {self.money}")
        print(f"Satiety – {self.satiety}")
        print(f"Gladness – {self.gladness}")
        print(f"Food – {self.home.food}")
        print(f"Mess – {self.home.mess}")
        print(f"Car Fuel – {self.car.fuel}")
        print(f"Car Strength – {self.car.strength}")
        if self.pet:
            print(f"Pet {self.pet.name} - Happiness: {self.pet.happiness}, Hunger: {self.pet.hunger}")

    def is_alive(self):
        if self.gladness < 0:
            print("Depression…")
            return False
        if self.satiety < 0:
            print("Dead…")
            return False
        if self.money < -500:
            print("Bankrupt…")
            return False

    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print("Settled in the house ")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"I bought a {self.car.brand} ")
        if self.job is None:
            self.get_job()
            print(f"I got a job as a {self.job.job} with a salary of {self.job.salary}")
        if self.pet is None:
            self.get_pet()

        self.days_indexes(day)

        if self.pet and self.pet.alive and random.randint(1, 3) == 1:
            self.care_for_pet()

        action = random.choice([self.eat, self.work, self.chill, self.clean_home, self.to_repair])
        action()



brands_of_car = {
    "BMW": {"fuel": 100, "strength": 100, "consumption": 6},
    "Lada": {"fuel": 50, "strength": 40, "consumption": 10},
    "Volvo": {"fuel": 70, "strength": 150, "consumption": 8},
    "Ferrari": {"fuel": 80, "strength": 120, "consumption": 14}
}


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("The car cannot move ")
            return False


class House:
    def __init__(self):
        self.mess = 0
        self.food = 0


job_list = {
    "Java developer": {"salary": 50, "gladness_less": 10},
    "Python developer": {"salary": 40, "gladness_less": 3},
    "C++ developer": {"salary": 45, "gladness_less": 25},
    "Rust developer": {"salary": 70, "gladness_less": 1}
}


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]



nick = Human(name="Nick")
for day in range(1, 800):
    if not nick.live(day):
        break