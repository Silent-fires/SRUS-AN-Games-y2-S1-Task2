import unittest

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from player import Player

class TestPlayer(unittest.TestCase):
    """Unit tests for the Player class."""

    def setUp(self):
        """Set up a Player instance for testing."""
        self.player = Player("1", "Tanmay")
        print(str(self.player))

    def test_initialisation(self):
        """Test Player initialisation."""
        self.assertEqual(self.player._ID, "1")
        self.assertEqual(self.player._Name, "Tanmay")

    def test_uid_property(self):
        """Test the uid property."""
        self.assertEqual(self.player._ID, "1")

    def test_name_property(self):
        """Test the name property."""
        self.assertEqual(self.player._Name, "Tanmay")

    def test_str_method(self):
        """Test the __str__ method."""
        self.assertEqual(str(self.player), "Player(ID=1, Name=Tanmay)")


if __name__ == "__main__":
    unittest.main()
