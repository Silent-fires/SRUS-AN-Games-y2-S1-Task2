from player import Player


class PlayerNode:
    """Node class for the doubly linked list that holds a Player instance."""

    def __init__(self, player):
        """
        Initializes a PlayerNode instance.

        Parameters:
            player (Player): The Player instance to store in the node.
        """
        self._player = player
        self._next = None
        self._prev = None

    @property
    def next(self) -> 'PlayerNode':
        """Gets the next PlayerNode."""
        return self._next

    @next.setter
    def next(self, next_node: 'PlayerNode') -> None:
        """Sets the next PlayerNode."""
        self._next = next_node

    @property
    def prev(self) -> 'PlayerNode':
        """Gets the previous PlayerNode."""
        return self._prev

    @prev.setter
    def prev(self, prev_node: 'PlayerNode') -> None:
        """Sets the previous PlayerNode."""
        self._prev = prev_node

    @property
    def key(self):
        """Gets the unique identifier of the Player."""
        return self._player.uid

    def __str__(self) -> str:
        """Returns a string representation of the PlayerNode."""
        # Get string id of prev and next nodes, if they exist.
        # if they don't exist, self.prev and or self.next are set to None.
        prev_str = str(self.prev._player.uid) if self.prev else "None"
        next_str = str(self.next._player.uid) if self.next else "None"
        return f"PlayerNode(-{self._player}, previous={prev_str}, next={next_str})"
        #return f"PlayerNode(player={self._player}, previous={prev_str}, next={next_str})"

    @property
    def player(self):
        """Gets the Player instance stored in the node."""
        return self._player


def main():
    """Main function to demonstrate the PlayerNode functionality."""
    # Assuming Player has a suitable __str__ method
    player = Player("1", "Tanmay")
    playerNode = PlayerNode(player)
    print(str(playerNode))


if __name__ == "__main__":
    main()
