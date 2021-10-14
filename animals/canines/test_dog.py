"""
These imports will work, and the imports in Dog should work due to the way we're
running unittest.
"""
from .dog import Dog
from unittest import TestCase, main

class DogUnitTests(TestCase):
    def setUp(self):
        self.dog = Dog("Nitro", "brown")

    def test_default_values_should_work(self):
        """
        Dog has two default values
        """
        self.assertEqual(self.dog.name, "Nitro")
        self.assertEqual(self.dog.color, "brown")

    def test_inherited_values_should_work(self):
        """
        Dog inherits from Mammal, which inherits from Animal
        """
        self.assertEqual(self.dog.eyes, 2)
        self.assertEqual(self.dog.living, True)
