from typing import TYPE_CHECKING

from player_list import PlayerList
from player import Player  # smart_lookup_table reached as well


class PlayerHashTable:
    SIZE = 42
    hash_map: list[PlayerList]

    def __init__(self):
        self.hash_map = [
            PlayerList() for _ in range(self.SIZE)]

    def get_index(self, hash_: int):
        return hash_ % self.SIZE

    def __getitem__(self, key: str) -> Player:          # get
        """Return a player by key"""
        index = self.get_index(Player.make_hash(key))
        player_list = self.hash_map[index]
        try:
            player_node = player_list.search(key)
            return player_node.player

        except ValueError as e:
            raise KeyError(str(e))

    def __setitem__(self, id: str, name: str):          # put
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

    def __delitem__(self, key) -> None:                 # remove
        player = self.__getitem__(key)
        index = self.get_index(hash(player))
        player_list = self.hash_map[index]
        try:
            player_list.deleteNode(key)
        except ValueError:
            pass

    def __len__(self):                                  # size v2
        count = 0
        for i, player_list in enumerate(self.hash_map):
            if not player_list:
                pass
            else:
                current_node = player_list._head  # using head as the start of the list
                while current_node:  # Iterate through the linked list
                    count = count + 1
                    current_node = current_node._next  # Move to the next node
        return count

    def display(self):                              # display
        """
        Prints the entire hash table, displaying each index and its associated PlayerList.
        
        This method iterates over the `hash_map`, which is a list of `PlayerList` objects. For each index,
        it prints the index and the players contained in the corresponding `PlayerList`.
        """
        for i, player_list in enumerate(self.hash_map):
            print(f"Index {i}: {player_list}")


def main():
    ph = PlayerHashTable()
    ph['1'] = 'Raf'
    ph['2'] = 'Faf'
    ph['4'] = 'gaf'
    ph['3'] = 'baw'
    # ph['1'] = 'Raf'
    # ph['2'] = 'Faf'
    print(ph['1'])
    print(ph['2'])
    print("")

    ph.__delitem__('2')

    ph.display()
    # print(ph['2'])
    print("")
    # ph['42']
    for pl, i in enumerate(ph.hash_map):
        # print(id(pl))
        # print(ph.get_index(id(pl)))
        # val = str(ph.get_index(id(pl)))
        ph[str(pl)] = 'added'
        print(ph[str(pl)])

    print("")
    ph.display()
    print("")
    print(ph.__len__())


if __name__ == '__main__':
    main()
