from player import Player
from player_node import PlayerNode
from typing import List


class PlayerList():

    def __init__(self, players: List[Player] = None):
        self._head: PlayerNode = None
        self._tail: PlayerNode = None

    def insert_first(self, player: Player) -> None:
        new_node = PlayerNode(player)
        if self._head:
            new_node.next = self._head  # Point new_node to the current head
            self._head.prev = new_node  # Update the current head's prev pointer
        self._head = new_node  # Update the head of the list to new_node
        if self._tail is None:  # List was empty before insertion
            self._tail = new_node

    def insert_last(self, player: Player) -> None:
        new_node = PlayerNode(player)
        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node  # Point new_node to the current tail
            new_node.prev = self._tail  # Update the current tail's prev pointer
            self._tail = new_node

    def display(self, forward: bool = True):
        testResult = []  # This will hold test results
        if forward:
            #print("--Head to Tail--")
            current = self._head
            while current:
                testResult.append(str(current._player))  # This will add test results
                print(current._player)
                current = current.next
        else:
            #print("--Tail to Head--")
            current = self._tail
            while current:
                testResult.append(str(current._player))  # This will add test results
                print(current._player)
                current = current.prev

        return " -> ".join(testResult)  # Join the results with " -> "

    def Delete_first(self) -> None:
        if self._head is None:
            # List is empty, nothing to delete
            return
        if self._head.next is not None:
            self._head.next.prev = None # update the prev pointer of the next node to none
        self._head = self._head.next

    def Delete_last(self) -> None:
        if self._head is None:
            # List is empty, nothing to delete
            return
        if self._head.next is None:
            # List has only one node
            self._head = None
            self._tail = None
            return

        # List has values delete the last one
        current = self._head
        while current.next.next is not None:
            current = current.next
        current.next = None
        self._tail = current

    def deleteNode(self, input_key):  # www.geeksforgeeks.org/python-program-for-deleting-a-node-in-a-linked-list/ (plus some modifications)
        if self._head is None:
            # List is empty, nothing to delete
            return

        # Check if the node to delete is the head node
        if self._head.key == input_key:
            self.Delete_first()
            return
        
        # Check if the node to delete is the tail node
        if self._tail.key == input_key:
            self.Delete_last()
            return
        
        previous = None
        current = self._head

        # Search the linked list to find the node to delete
        while (current is not None):
            if current.key == input_key:
                break
            previous = current
            current = current.next

        # If the node was not found, exit the function
        if current is None:
            return

        # update the prev pointer of the next node
        if current.next is not None:
            current.next.prev = previous

        # Bypass the node to be deleted. ('prev, node, next' | prev.next = next | 'prev, next')
        previous.next = current.next

    def __str__(self) -> str:
        if self.is_empty():
            return "List is empty"

        current = self._head
        nodes = []
        """while 'current' has value append each iteration of 'current' to the list called nodes"""
        while current:
            nodes.append(str(current))
            current = current.next
        return "  ->  ".join(nodes)

    def is_empty(self) -> bool:
        return self._head is None


def main():
    pass

    pl = PlayerList()

    print("")
    pl.insert_first(Player("3", "Bob"))
    print(pl)  # Should print: Bob
    print("")

    pl.insert_first(Player("1", "Tanmay"))
    pl.insert_first(Player("2", "Alice"))
    print(pl)  # Should print: Alice -> Tanmay -> Bob
    print("")

    pl.insert_last(Player("1", "Tanmay"))
    print(pl)  # Should print: Alice -> Tanmay -> Bob -> Tanmay
    print("")

    pl.display(True)
    print("")
    pl.display(False)
    print("")

if __name__ == "__main__":
    main()
