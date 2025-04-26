from typing import TYPE_CHECKING

from player_list import PlayerList
from player import Player


class PlayerHashTable:
    SIZE = 42
    hash_map: list[PlayerList]

    def __init__(self):
        self.hash_map = [
            PlayerList() for _ in range(self.SIZE)]

    def get_index(self, hash_: int):
        return hash_ % self.SIZE

    def __getitem__(self, key: str) -> Player:
        """Return a player by key"""
        index = self.get_index(Player.make_hash(key))
        player_list = self.hash_map[index]
        try:
            player_node = player_list.search(key)
            return player_node.player

        except ValueError as e:
            raise KeyError(str(e))

    def __setitem__(self, id, name):
        player = Player(id, name)
        index = self.get_index(hash(player))
        player_list = self.hash_map[index]
        try:
            node = player_list.search(id)
            node.Player = player
        except ValueError:
            player_list.insert_first(player)

        # hash the player
        # see if player in list
        # if yes, replace player
        # else append player

    def remove(self, key) -> None:
        player = self.__getitem__(key)
        index = self.get_index(hash(player))
        player_list = self.hash_map[index]
        try:
            player_list.deleteNode(key)
        except ValueError:
            pass

    def size(self):
        count = 0
        for i in self.table:
            if not i:
                pass
            else:
                count = count + 1
        return count


def main():
    ph = PlayerHashTable()
    ph['1'] = 'Raf'
    ph['2'] = 'Faf'
    print(ph['1'])
    print(ph['2'])
    print("")

    ph.remove('2')

    print(ph['1'])
    # print(ph['2'])
    print("")
    # ph['42']
    for pl in ph.hash_map:
        print(id(pl))


if __name__ == '__main__':
    main()
