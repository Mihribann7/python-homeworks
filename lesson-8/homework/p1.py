class Animal:
    def __init__(self, breed, age):
        self.__breed = breed
        self.__age = age

    def makeSound(self):
        print("Making a sound")

class Dog(Animal):
    def __init__(self, breed, age, color):
        super().__init__(breed, age)
        self.__color = color

    def makeSound(self):
        print("Woaw")

class Cat(Animal):
    def __init__(self, breed, age, fur):
        super().__init__(breed, age)
        self.__fur = fur
    def makeSound(self):
        print("Meow")

cat = Cat("Lll", 12, "fluffy")
cat.makeSound()