# Example of a simple class
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        return f"{self.name} says woof!"

my_dog = Dog("Rex", "German Shepherd")
print(my_dog.bark())
