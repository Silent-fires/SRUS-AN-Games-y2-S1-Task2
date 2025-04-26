import unittest

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from player import Player
from player_list import PlayerList

class TestPlayerList(unittest.TestCase):
    """Unit tests for the PlayerList class."""

    def setUp(self) -> None:
        """Reset the PlayerList before each test."""
        self.player_list = PlayerList()
        
    def test_empty_list(self):
        """Test behavior of empty list."""
        self.assertTrue(self.player_list.is_empty())
        
        self.player_list.insert_first(Player("8", "keb"))
        self.assertFalse(self.player_list.is_empty())


    def test_insert_first(self):
        """Test inserting players at the beginning."""
        self.player_list.insert_first(Player("77", "jakeb"))
        self.player_list.insert_first(Player("78", "jakeb"))
        self.player_list.insert_first(Player("8", "keb"))
        
        # Expected order is 8 -> 78 -> 77
        expected = ("PlayerNode(-Player(ID=8, Name=keb), previous=None, next=78)  ->  PlayerNode(-Player(ID=78, "
                    "Name=jakeb), previous=8, next=77)  ->  PlayerNode(-Player(ID=77, Name=jakeb), previous=78, "
                    "next=None)")
        self.assertEqual(str(self.player_list), expected)

    def test_insert_last(self):
        """Test inserting players at the end."""
        self.player_list.insert_last(Player("8", "keb"))
        self.player_list.insert_last(Player("77", "jakeb"))
        self.player_list.insert_last(Player("78", "jakeb"))

        # Expected order is 8 -> 77 -> 78
        expected = ("PlayerNode(-Player(ID=8, Name=keb), previous=None, next=77)  ->  PlayerNode(-Player(ID=77, "
                    "Name=jakeb), previous=8, next=78)  ->  PlayerNode(-Player(ID=78, Name=jakeb), previous=77, "
                    "next=None)")
        self.assertEqual(str(self.player_list), expected)


    def test_delete_first(self):
        """Test deleting the first player."""
        self.player_list.insert_first(Player("77", "jakeb"))
        self.player_list.insert_first(Player("78", "jakeb"))
        self.player_list.insert_first(Player("8", "keb"))

        self.player_list.Delete_first()
        
        # Expected order after deleting the first player is 78 -> 77
        expected = ("PlayerNode(-Player(ID=78, Name=jakeb), previous=None, next=77)  ->  PlayerNode(-Player(ID=77, "
                    "Name=jakeb), previous=78, next=None)")
        self.assertEqual(str(self.player_list), expected)

    def test_noneDelete_first(self):
        """Test deleting the first player."""
        self.player_list.Delete_first()
        
        # Expected order after deleting the first player is 78 -> 77
        expected = 'List is empty'
        self.assertEqual(str(self.player_list), expected)

    def test_delete_last(self):
        """Test deleting the last player."""
        self.player_list.insert_last(Player("8", "keb"))
        self.player_list.insert_last(Player("77", "jakeb"))
        self.player_list.insert_last(Player("78", "jakeb"))

        self.player_list.Delete_last()
        
        # Expected order after deleting the last player is 8 -> 77
        expected = ("PlayerNode(-Player(ID=8, Name=keb), previous=None, next=77)  ->  PlayerNode(-Player(ID=77, "
                    "Name=jakeb), previous=8, next=None)")
        self.assertEqual(str(self.player_list), expected)

    def test_noneDelete_last(self):
        """Test deleting the first player."""
        self.player_list.Delete_last()
        
        # Expected order after deleting the first player is 78 -> 77
        expected = 'List is empty'
        self.assertEqual(str(self.player_list), expected)

    def test_delete_nodes(self):
        """Test deleting a specific node by player ID."""
        self.player_list.insert_last(Player("8", "keb"))
        self.player_list.insert_last(Player("77", "jakeb"))
        self.player_list.insert_last(Player("78", "jakeb"))

        self.player_list.deleteNode("7")
        # Expected order ID 8 -> 77 -> 78
        expected = ("PlayerNode(-Player(ID=8, Name=keb), previous=None, next=77)  ->  PlayerNode(-Player(ID=77, "
                    "Name=jakeb), previous=8, next=78)  ->  PlayerNode(-Player(ID=78, Name=jakeb), previous=77, "
                    "next=None)")
        self.assertEqual(str(self.player_list), expected)

        self.player_list.deleteNode("77")
        # Expected order after deleting node with ID "77" is 8 -> 78
        expected = ("PlayerNode(-Player(ID=8, Name=keb), previous=None, next=78)  ->  PlayerNode(-Player(ID=78, "
                    "Name=jakeb), previous=8, next=None)")
        self.assertEqual(str(self.player_list), expected)

        self.player_list.deleteNode("8")
        # Expected order after deleting node with ID "8" is 78
        expected = "PlayerNode(-Player(ID=78, Name=jakeb), previous=None, next=None)"
        self.assertEqual(str(self.player_list), expected)

        self.player_list.deleteNode("78")
        expected = 'List is empty'
        self.assertEqual(str(self.player_list), expected)

        self.player_list.deleteNode("7")
        expected = 'List is empty'
        self.assertEqual(str(self.player_list), expected)


    def test_displayForward(self):
        """Test display head to tail."""
        self.player_list.insert_last(Player("8", "keb"))
        self.player_list.insert_last(Player("77", "jakeb"))
        self.player_list.insert_last(Player("78", "jakeb"))

        output = self.player_list.display(True)
        # Expected order after deleting the last player is 8 -> 77
        expected = "Player(ID=8, Name=keb) -> Player(ID=77, Name=jakeb) -> Player(ID=78, Name=jakeb)"
        self.assertEqual(output, expected)

    def test_displayBack(self):
        """Test display tail to head."""
        self.player_list.insert_last(Player("8", "keb"))
        self.player_list.insert_last(Player("77", "jakeb"))
        self.player_list.insert_last(Player("78", "jakeb"))

        output = self.player_list.display(False)
        # Expected order after deleting the last player is 8 -> 77
        expected = "Player(ID=78, Name=jakeb) -> Player(ID=77, Name=jakeb) -> Player(ID=8, Name=keb)"
        self.assertEqual(output, expected)


        
if __name__ == "__main__":
    unittest.main()
