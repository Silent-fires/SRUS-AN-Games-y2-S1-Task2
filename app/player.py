
class Player:

    def __init__(self, ID: str, PlayerName: str):
        self._ID = ID
        self._PlayerName = PlayerName

    def __str__(self) -> str:
        return f"Player(ID={self._ID}, Name={self._PlayerName})"

    @property
    def uid(self):
        return self._ID

    @uid.setter
    def uid(self, player_id: 'Player') -> None:
        self._ID = player_id

    @property
    def name(self):
        return self._PlayerName

    @name.setter
    def name(self, player_name: 'Player') -> None:
        self._PlayerName = player_name


def main():
    # Assuming Player has a suitable __str__ method
    player = Player("1", "Tanmay")
    print(str(player))

    print(str(player.uid))
    print(str(player.name))

if __name__ == "__main__":
    main()
