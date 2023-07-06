# Creating a Class
class Dog():
    def __init__(self, name):
        self.name = name
    def sit(self):
        print(self.name + " is sitting.")


my_dog = Dog('Peso')
print(my_dog.name + " is a great dog!")
my_dog.sit()