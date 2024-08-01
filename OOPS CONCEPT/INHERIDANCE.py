class Animal:
    def __init__(self,species):
        self.species=species
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return "woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!!"
dog=Dog("Dog")
cat=Cat("Cat")
print(f"{dog.species} says {dog.speak()}")
print(f"{cat.species} says {cat.speak()}")


