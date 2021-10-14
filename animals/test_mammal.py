"""
Keeping this file in the same folder with mammal.py allows for easy import.
"""
from .mammal import Mammal
from unittest import TestCase, main

class MammalUnitTests(TestCase):
    """
    Specify tests for the Mammal class.
    """
    def setUp(self):
        self.mammal = Mammal()
    
    def test_should_have_two_eyes(self):
        """
        Test default values.
        """
        self.assertEqual(self.mammal.eyes, 2)