class Mom:
    def __init__(self, height):
        self.height = height

    def cook(self):
        return "Mom can cook delicious meals."

class Dad:
    def __init__(self, weight):
        self.weight = weight

    def drive(self):
        return "Dad is good at driving a car."

class Son(Mom, Dad):
    def __init__(self, height, weight, humor):
        Mom.__init__(self, height)
        Dad.__init__(self, weight)
        self.humor = humor

    def joke(self):
        return f"Son jokes: {self.humor}"


son = Son(height=180, weight=75, humor="Why did the chicken cross the road? To get to the other side!")


print(son.height)
print(son.weight)
print(son.joke())
print(son.cook())
print(son.drive())