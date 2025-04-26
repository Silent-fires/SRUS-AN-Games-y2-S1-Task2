import unittest

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player("1", "Tanmay")
        print(str(self.player))

    def test_initilization(self):
        self.assertEqual(self.player._ID, "1")
        self.assertEqual(self.player._PlayerName, "Tanmay")

    def test_uid_property(self):
        self.assertEqual(self.player._ID, "1")

    def test_name_property(self):
        self.assertEqual(self.player._PlayerName, "Tanmay")

    def test_str_method(self):
        self.assertEqual(str(self.player), "Player(ID=1, Name=Tanmay)")


if __name__ == "__main__":
    unittest.main()
