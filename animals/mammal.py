from . animal import Animal

class Mammal(Animal):
    def __init__(self):
        self.eyes = 2
        super().__init__()

# # Mammal and Animal are in the same folder. Easy import.
# if __name__ == "__main__":
#     test_mammal = Mammal()
#     print("testing animal class")
#     print(test_mammal.living, test_mammal.eyes)