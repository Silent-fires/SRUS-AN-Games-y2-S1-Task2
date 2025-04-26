import unittest
from io import StringIO

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from player_hash_table import PlayerHashTable
from smart_lookup_table import SmartLookupTable


def printCheck(self, expected_outputs, output):
    """expected_outputs must be in order of index or error occurs"""
    lines = len(output.splitlines())  # Split the output into lines

    for i in range(lines):
        if i >= len(expected_outputs) or not expected_outputs[i]: # Check if no entry at index i
            expected_outputs.insert(i, f"Index {i}: []")
        elif f"Index {i}:" not in expected_outputs[i]:  # Check if entry at index i is of correct index
            expected_outputs.insert(i, f"Index {i}: []")

    # Check that all expected-outputs are in the actual output
    for expected in expected_outputs:
        self.assertIn(expected, output)

    # Check that the output 'only' contains the expected-outputs
    for line in output.splitlines():
        self.assertTrue(any(expected in line for expected in expected_outputs),
                        f"Unexpected line in output: {line}")



class TestHashTable(unittest.TestCase):
    """Unit tests for the PlayerHashTable class."""

    def setUp(self) -> None:
        """Reset the PlayerHashTable before each test."""
        self.ph = PlayerHashTable()
        self.ph['1'] = 'Raf'
        self.ph['2'] = 'Faf'
        self.ph['4'] = 'gaf'
        self.ph['3'] = 'baw'

    def testDisplay(self):
        """Test correct display of players."""
        # Redirect stdout to a StringIO object to capture the print output
        sys.stdout = StringIO()

        # Call the display method
        self.ph.display()

        # Get the output from the StringIO object
        output = sys.stdout.getvalue()

        expected_outputs = [
            "Index 1: PlayerNode(-Player(ID=1, Name=Raf), previous=None, next=None)",
            "Index 20: PlayerNode(-Player(ID=3, Name=baw), previous=None, next=None)",
            "Index 27: PlayerNode(-Player(ID=4, Name=gaf), previous=None, next=None)",
            "Index 35: PlayerNode(-Player(ID=2, Name=Faf), previous=None, next=None)"
        ]

        printCheck(self, expected_outputs, output)

    def testInsertNewPlayer(self):
        """Test inserting a new player."""
        self.ph['5'] = 'Zoe'
        sys.stdout = StringIO()
        self.ph.display()
        output = sys.stdout.getvalue()

        expected_outputs = [
            "Index 1: PlayerNode(-Player(ID=1, Name=Raf), previous=None, next=None)",
            "Index 4: PlayerNode(-Player(ID=5, Name=Zoe), previous=None, next=None)",  # new
            "Index 20: PlayerNode(-Player(ID=3, Name=baw), previous=None, next=None)",
            "Index 27: PlayerNode(-Player(ID=4, Name=gaf), previous=None, next=None)",
            "Index 35: PlayerNode(-Player(ID=2, Name=Faf), previous=None, next=None)"
        ]

        printCheck(self, expected_outputs, output)

    def testUpdatePlayer(self):
        """Test updating an existing player."""
        self.ph['2'] = 'Sof'
        sys.stdout = StringIO()
        self.ph.display()
        output = sys.stdout.getvalue()

        expected_outputs = [
            "Index 1: PlayerNode(-Player(ID=1, Name=Raf), previous=None, next=None)",
            "Index 20: PlayerNode(-Player(ID=3, Name=baw), previous=None, next=None)",
            "Index 27: PlayerNode(-Player(ID=4, Name=gaf), previous=None, next=None)",
            "Index 35: PlayerNode(-Player(ID=2, Name=Sof), previous=None, next=None)"
        ]

        printCheck(self, expected_outputs, output)

    def testDeletePlayer(self):
        """Test deleting an existing player."""
        self.ph.__delitem__('2')
        sys.stdout = StringIO()
        self.ph.display()
        output = sys.stdout.getvalue()

        expected_outputs = [
            "Index 1: PlayerNode(-Player(ID=1, Name=Raf), previous=None, next=None)",
            "Index 20: PlayerNode(-Player(ID=3, Name=baw), previous=None, next=None)",
            "Index 27: PlayerNode(-Player(ID=4, Name=gaf), previous=None, next=None)",
            "Index 35: PlayerNode(-Player(ID=2, Name=Faf), previous=None, next=None)"
        ]

        # AssertionError: 'Index 35: PlayerNode(-Player(ID=2, Name=Faf), previous=None, next=None)' not found
        with self.assertRaises(Exception):
            printCheck(self, expected_outputs, output)



class TestLookupTable(unittest.TestCase):
    """Unit tests for the SmartLookupTable class."""

    def setUp(self) -> None:
        """Reset the SmartLookupTable before each test."""
        self.SMT = SmartLookupTable()
        self.SMT.insert(56, "YO yo hi")
        self.SMT.insert(3, "hi")
        self.SMT.insert(64, "YO bob")
        self.SMT.insert(72, "Ya bob")

    def testDisplay(self):
        # Redirect stdout to a StringIO object to capture the print output
        sys.stdout = StringIO()

        # Call the display method
        self.SMT.display()

        # Get the output from the StringIO object
        output = sys.stdout.getvalue()

        # Define the expected output strings
        expected_outputs = [
            "Index 1: [(64, 'YO bob')]",
            "Index 2: [(56, 'YO yo hi'), (72, 'Ya bob')]",
            "Index 3: [(3, 'hi')]"
        ]
        
        printCheck(self, expected_outputs, output)

    def testInsertNewPlayer(self):
        """Test inserting a new player."""
        self.SMT.insert(5, "Zoe")
        sys.stdout = StringIO()
        self.SMT.display()
        output = sys.stdout.getvalue()

        expected_outputs = [
            "Index 1: [(64, 'YO bob')]",
            "Index 2: [(56, 'YO yo hi'), (72, 'Ya bob')]",
            "Index 3: [(3, 'hi')]",
            "Index 8: [(5, 'Zoe')]"
        ]

        printCheck(self, expected_outputs, output)

    def testUpdatePlayer(self):
        """Test updating an existing player."""
        self.SMT.insert(72, "Sof")
        sys.stdout = StringIO()
        self.SMT.display()
        output = sys.stdout.getvalue()

        expected_outputs = [
            "Index 1: [(64, 'YO bob')]",
            "Index 2: [(56, 'YO yo hi'), (72, 'Sof')]",
            "Index 3: [(3, 'hi')]"
        ]

        printCheck(self, expected_outputs, output)

    def testRemovePlayer(self):
        """Test removing an existing player."""
        self.SMT.remove(72)
        # self.SMT.remove('72')  # if key is of wrong type, KeyError will occur.

        sys.stdout = StringIO()
        self.SMT.display()
        output = sys.stdout.getvalue()

        expected_outputs = [
            "Index 1: [(64, 'YO bob')]",
            "Index 2: [(56, 'YO yo hi'), (72, 'Ya bob')]",
            "Index 3: [(3, 'hi')]"
        ]

        # KeyError: 'Matching key 72 not found'
        with self.assertRaises(Exception):
            printCheck(self, expected_outputs, output)


if __name__ == "__main__":
    unittest.main()
    print("")
