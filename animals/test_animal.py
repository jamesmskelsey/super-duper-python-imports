"""
Keeping this file in the same folder with animal.py allows for easy import.
"""
from .animal import Animal
from unittest import TestCase, main

class AnimalUnitTests(TestCase):
    """
    Specify tests for the animal class.
    """
    def setUp(self):
        self.animal = Animal()
    
    def test_should_be_alive(self):
        """
        Test default values.
        """
        self.assertEqual(self.animal.living, True) # Iiiiit's... ALIVE!