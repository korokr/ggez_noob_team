class Dog:

    amount_dogs = 0
    def __init__(self, name, age, weight, color, breed, ):
        Dog.amount_dogs += 1
        self.name = name
        self.age = age
        self.weight = weight
        self.color = color
        self.breed =  breed

    def GetFullInfo(self):
        return f"Name: {self.name}\nAge: {self.age}\nWeight: {self.weight}\nColor: {self.color}\nBreed: {self.breed}"