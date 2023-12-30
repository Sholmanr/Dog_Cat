class Dog:

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def bark(self):
        print("bark, bark\n  bark, bark\n")

    def rollOver(self):
        print(f"{self.name} rolls over\n")

    def catch(self):
        print(f"{self.name} caught the treat\n")