from pearson import pearson_hash


class Player:
    """Represents a player with a unique ID, name, and hashed password."""

    def __init__(self, ID: str, Name: str):
        """
        Initialises a Player instance.

        Parameters:
            ID (str): The unique identifier for the player.
            Name (str): The name of the player.
        """
        self._ID = ID
        self._Name = Name

    def __str__(self) -> str:
        """Returns a string representation of the Player instance."""
        return f"Player(ID={self._ID}, Name={self._Name})"

    @property
    def uid(self):
        """Gets the player's unique ID."""
        return self._ID

    @uid.setter
    def uid(self, player_id: 'Player') -> None:
        """Sets the player's unique ID."""
        self._ID = player_id

    @property
    def name(self):
        """Gets the player's name."""
        return self._Name

    @name.setter
    def name(self, player_name: 'Player') -> None:
        """Sets the player's name."""
        self._Name = player_name

    def __hash__(self) -> int:
        return self.make_hash(self.uid)

    @staticmethod
    def make_hash(key):
        return pearson_hash(key)


def main():
    """Main function to demonstrate the Player class functionality."""
    # Assuming Player has a suitable __str__ method
    player = Player("1", "Tanmay")
    print(str(player))
    print("")

    print(str(player.uid))
    print(str(player.name))
    print("")

    print(player.__hash__())

    # debug
    # print(f"Player(ID={player.uid}, Name={player.name}")


if __name__ == "__main__":
    main()
