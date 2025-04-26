import random
import pearson
from typing import Hashable

random.seed(42)


class SmartLookupTable[K: Hashable, T]:
    SIZE = 10  # max = 256
    pearson_table = list(range(SIZE))  # Max 256
    random.shuffle(pearson_table)
    table = list[T | None]

    def __init__(self):
        self.table = [[] for _ in range(self.SIZE)]

    def p_hash(self, key: K) -> int:
        key = str(key)
        key = bytes(key, encoding='utf8')
        hash_ = 0
        for b in key:
            hash_ = self.pearson_table[(hash_ ^ b) % self.SIZE]
        return hash_

    def insert(self, key: K, value: T) -> None:         # put
        position = self.p_hash(key)

        if any(k == key for k, v in self.table[position]):
            self.remove(key)
        self.table[position].append((key, value))

    def _find_matching_key(self, target: K, candidates: list) -> int:
        for i, (k, *_) in enumerate(candidates):
            if k == target:
                return i
        raise KeyError(
            f"Matching key {target} not found")

    def get(self, key: K) -> T:                         # get
        position = self.p_hash(key)
        item = self.table[position]
        if not item:
            raise KeyError(f"Matching key {key} not found")

        return item[self._find_matching_key(key, item)]

    def remove(self, key: K) -> None:                   # remove
        position = self.p_hash(key)
        item = self.table[position]  # find item in list
        item.remove(item[self._find_matching_key(key, item)])

    def size(self):                                     # size
        count = 0
        for i in self.table:
            if not i:
                pass
            else:
                for j in i:
                    count = count + 1
        return count

    def display(self):                                  # display
        for i, n in enumerate(self.table):
            print(f"Index {i}: {n}")


if __name__ == "__main__":
    SMT = SmartLookupTable()
    SMT.insert(56, "YO yo hi")
    SMT.insert(3, "hi")
    SMT.insert(74, "YO bob")
    SMT.insert(72, "Ya bob")
    SMT.insert(9, "ggg")

    SMT.insert("Jane", "YO yo hi")
    SMT.insert("Janis", "hi")

    SMT.insert("Axel", "YO bob")

    SMT.insert("cass", "Ya bob")
    SMT.insert("ssac", "ggg")

    SMT.insert("zzz", "Yab bob")

    file = SMT.get(56)
    print(file, "  get1")

    # file = SMT.get(7)
    # print(file)

    file = SMT.get("Jane")
    print(file, "  get2")
    file = SMT.get("cass")
    print(file, "  get3")
    file = SMT.get("ssac")
    print(file, "  get4")

    print("Pearsons:")
    print(SMT.p_hash("aaaaaa"))
    print(SMT.p_hash("aaaaab"))
    print(SMT.p_hash("baaaaa"))
    # file = SMT.get(1)
    # print(file)
    print("")
    print(SMT.table)
    print(SMT.size())
    print("")
    SMT.remove("Janis")
    print(SMT.table)
    print(SMT.size())
    print("")
    SMT.remove("ssac")
    SMT.insert(72, "Sof")
    print(SMT.table)
    print(SMT.size())

    print("")
    print("")

    SMT.display()

