import Dog as dog
import Cat as cat

proceed = True
pet_type = input("Do you have a dog or a cat?\n")

if pet_type == "dog":
    name = input("What is your dog's name?\n")
    age = int(input("How old is your dog?\n"))
    breed = input("What breed is your dog?\n")
    new_dog = dog.Dog(name, age, breed)
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



elif pet_type == "cat":
    name = input("What is your cat's name?\n")
    age = input("How old is your cat?\n")
    new_cat = cat.Cat(name, age)

