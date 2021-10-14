from random import randint
from ..mammal import Mammal

class Dog(Mammal):
    def __init__(self, name, color):
        self.name = name
        self.color = color
        super().__init__()

    def __str__(self):
        return f"{self.name} is a {self.color} {randint(11, 15)}/10 good boy."

# This, at this point, throws this error:
# ImportError: attempted relative import with no known parent package
# # if the file is run from the canines folder.
# if __name__ == "__main__":
#     test_dog = Dog("Fido", 8)
#     print("testing animal class")
#     print(test_dog.living, test_dog.eyes, test_dog)