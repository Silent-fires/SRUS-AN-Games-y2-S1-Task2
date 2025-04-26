import unittest
from io import StringIO

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from player_hash_table import PlayerHashTable
from smart_lookup_table import SmartLookupTable


def printCheck(self, expected_outputs, output):
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




if __name__ == "__main__":
    unittest.main()
    print("")
