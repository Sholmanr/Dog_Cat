"""This program gets the user's pets and stores them in a list

"""
import Dog as dog
import Cat as cat

proceed = True
more = True
pets = []

pet_type = input("Do you have a dog or a cat?\n")

while more:
    if pet_type == "dog":
        name = input("What is your dog's name?\n")
        age = int(input("How old is your dog?\n"))
        breed = input("What breed is your dog?\n")
        new_dog = dog.Dog(name, age, breed)
        pets
        while proceed:
            choice = int(input("What would you like to do?\n" +
                           "1. Knock on the door\n"
                           "2. Tell the dog to roll over\n"
                           "3. Throw " + new_dog.name + " a treat\n"))

            match choice:
                case 1:
                    new_dog.bark()
                case 2:
                    new_dog.rollOver()
                case 3:
                    new_dog.catch()

            cont = input("Would you like to continue? y/n")

            if cont.lower() == "n" or cont.lower() == "no":
                proceed = False

            elif cont.lower() == "y" or cont.lower() == "yes":
                proceed = True


    elif pet_type == "cat":
        name = input("What is your cat's name?\n")
        age = input("How old is your cat?\n")
        new_cat = cat.Cat(name, age)
        while proceed:
            choice = int(input("What would you like to do?\n" +
                           "1. Look at " + new_cat.name + "\n" +
                           "2. Pet " + new_cat.name + "'s belly\n" +
                           "3. Make a loud noise\n" +
                            "4. SLowly approach " + new_cat + " and pet them\n"))

            match choice:
                case 1:
                    new_cat.meow()
                case 2:
                    new_cat.hiss()
                case 3:
                    new_cat.runAway()
                case 4:
                    new_cat.purr()

            cont = input("Would you like to continue? y/n\n")

            if cont.lower() == "n" or cont.lower() == "no":
                proceed = False

            elif cont.lower() == "y" or cont.lower() == "yes":
                proceed = True


