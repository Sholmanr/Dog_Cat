class Cat:

    def __init__(self, name, age):
        """ Initialize Cat object"""
        self.name = name
        self.age = age

    def meow(self):
        print("Meow\n")

    def hiss(self):
        print("Hiss\n")

    def runAway(self):
        print(f"{self.name} scurries away!\n")

    def purr(self):
        print(f"{self.name} is vibrating\n"
              f"Purrrrrr\n")
            
    def scratch(self):
        print(f"{self.name} scratched you \n")