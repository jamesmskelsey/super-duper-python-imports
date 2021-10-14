"""
If you run 'py main.py' from the top level folder, it will happily allow this to work.

Animal -> Mammal -> Dog

Dog is in the canine folder, and inherits from Mammal in the previous folder, which inherits
from Animal in that same folder.

However, if you try to run the dog.py file, you will get an ImportError. 
"""
from animals.canines.dog import Dog

test_dog = Dog("Fido", 8)
print("Testing dog class import")
print(test_dog)
print(f"{'Is alive' if test_dog.living else 'Not alive'} and has {test_dog.eyes} eyes")