import random
from typing import TypeVar, Hashable

random.seed(42)
pearson_table = list(range(256))
random.shuffle(pearson_table)


class SmartLookupTable[K: Hashable, T]:
    SIZE = 20  # max = 256
    table = list[T | None]

    def __init__(self):
        # self.table = [None] * self.SIZE
        self.table = [[] for _ in range(self.SIZE)]
        # self.table = [[]] * self.SIZE  # BAD, dont use

    def p_hash(self, key):
        key = bytes(key, encoding='utf8')
        hash_ = 0
        for b in key:
            hash_ = pearson_table[hash_ ^ b]
        return hash_

    def _hash(self, key: K) -> int:
        key = str(key)
        if len(key) == 0:
            raise ValueError
        return sum(map(ord, key)) % self.SIZE

    def insert(self, key: K, value: T) -> None:
        position = self._hash(key)
        self.table[position].append((key, value))

    def _find_matching_key(self, target: K, candidates: list) -> int:
        for i, (k, *_) in enumerate(candidates):
            if k == target:
                return i
        raise KeyError(
            f"Matching key {target} not found")

    def get(self, key: K) -> T:
        position = self._hash(key)
        item = self.table[position]
        if not item:
            raise KeyError(f"Matching key {key} not found")

        return item[self._find_matching_key(key, item)]

    def remove(self, key: K) -> None:
        position = self._hash(key)
        self.table[position] = []

    def size(self):
        count = 0
        for i in self.table:
            if not i:
                pass
            else:
                count = count + 1
        return count


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

    print("Not so good hash:")
    print(SMT._hash("aaaaaa"))
    print(SMT._hash("aaaaab"))
    print(SMT._hash("baaaaa"))

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
    print(SMT.table)
    print(SMT.size())
