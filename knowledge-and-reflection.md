# Overview

These questions are designed to accompany the task "Implementing a Hash Map in Python" in the "Data Structures and Algorithms" module. The questions are intended to test your understanding of hash maps, their implementation in Python, and the process of integrating data from a double linked list into a hash map. You will also be asked to reflect on your learning and the challenges you faced during the task.

# Knowledge questions

The following are all examples of hash functions:

```python
# (1) the simplest hash function (Stupidly Simple Hash)
def ssh(key):
    return 1
```

```python
# (2) hash function that sums the ASCII values of the characters in the key
def sum_of_ascii_values(key: str, size: int) -> int:
    total = 0
    for char in key:
        total += ord(char)
    return total % size
```

A more Pythonic version

```python
# (2a)
def sum_of_ascii_values(key: str, size: int) -> int:
    return sum(ord(char) for char in key) % size
```

A Pearson Hash function

```python
# (3) Pearson hash function
# https://en.wikipedia.org/wiki/Pearson_hashing
import random

random.seed(42)

# This is INCORRECT:
# pearson_table = [random.randint(0, 255) for _ in range(256)]
pearson_table = list(range(256))
random.shuffle(pearson_table)

def pearson_hash(key: str, size: int) -> int:
    hash_ = 0
    for char in key:
        hash_ = pearson_table[hash_ ^ ord(char)]
    return hash_ % size
```

The following is a hash function that uses the built-in `hash` function in Python

```python
# (4) hash function that uses the built-in hash function
def built_in_hash(key: str, size: int) -> int:
    return hash(key) % size
```

Finally, the following is a hash function that uses the `SHA256` hash function from the `hashlib` module

```python
# (5) hash function that uses the SHA256 hash function
# https://docs.python.org/3/library/hashlib.html
# https://en.wikipedia.org/wiki/SHA-2
# https://en.wikipedia.org/wiki/SHA-2#Pseudocode
import hashlib

def sha256_hash(key: str, size: int) -> int:
    return int(hashlib.sha256(key.encode()).hexdigest(), 16) % size
```

1. All of the above functions are hash functions. Explain how so - what key properties do they all share?

> Hash functions take an input (key) and return a fixed-size 
> number (hash); All the functions listed above do this, thus 
> fit the description and requirements to be hash functions.

2. What are the advantages and disadvantages of each of the above hash functions? Evaluate in terms of uniformity, determinism, efficiency, collision resistance, sensitivity to input changes, and security[1](#Reference). You may need to do some research to answer this question 😱

> 1. ssh():
>    1. Uniformity: Poor. All inputs map to the same hash value.
>    2. Determinism: Yes. Always returns 1 for any input.
>    3. Efficiency: Very efficient, but very poor functionality.
>    4. Collision Resistance: None.
>    5. Sensitivity to Input Changes: None.
>    6. Security: None.
> 
> 2. sum_of_ascii_values():
>    1. Uniformity: Moderate.
>    2. Determinism: Yes.
>    3. Efficiency: Moderate. Iterates over each character in the input string.
>    4. Collision Resistance: Low. Different inputs can have the same sum.
>    5. Sensitivity to Input Changes: Linear. A small change in input 
>    (key) results in a proportional change in the hash value.
>    6. Security: None.
> 
> 3. pearson_hash():
>    1. Uniformity: Good. Designed for uniformed distribution. 
>    2. Determinism: Yes.
>    3. Efficiency: High.
>    4. Collision Resistance: Moderate. Collision is more likely with large datasets.
>    5. Sensitivity to Input Changes: High. A small change in input 
>    leads to a significantly different hash value.
>    6. Security: Low. 
> 
> 4. built_in_hash():
>    1. Uniformity: Good.
>    2. Determinism: Yes.
>    3. Efficiency: Very efficient.
>    4. Collision Resistance: Moderate. Collision is more likely with large datasets.
>    5. Sensitivity to Input Changes: High. A small change in input 
>    leads to a significantly different hash value.
>    6. Security: Moderate. But not very suitable.
> 
> 5. sha256_hash():
>    1. Uniformity: Good. Designed for uniformed distribution. 
>    2. Determinism: Yes.
>    3. Efficiency: Moderate to low.
>    4. Collision Resistance: Extremely high.
>    5. Sensitivity to Input Changes: High. A small change in input 
>    leads to a significantly different hash value.
>    6. Security: High. Designed for security.

3. List the three most important attributes (arranged from most to least) in the context of a hash map? Justify your answer.

> I would say the most important attributes would be Collision-Resistance,
> either Uniformity or Determinism, and finally Efficiency.
> 1. Collision-Resistance: Hash maps are designed for fast access, but if
>   the information isn't there or has been overwritten speed doesn't really
>   matter. Preventing collisions should be the top focus, improving the
>   reliability and scalability of the hash map.
> 2. Uniformity/Determinism: To me these two attributes hold similar weight
>   and value. Without Uniformity the hash map could become unbalanced and
>   more prone to collisions. And without Determinism keys won’t map back 
>   to the same hash consistently, making lookups unreliable. Between the two
>   Uniformity improves performance, while Determinism is more a requirement.
> 3. Efficiency: A hash map’s performance relies heavily on how fast the 
>   hash function can compute an index. Every single operation depends on the 
>   speed of the hash function, if the hash slow, even basic operations become 
>   sluggish, and from my research performance-critical systems 
>   such as databases and web servers compound this delay quickly.

4. Which of the above hash functions would you choose to implement the requirements of the task? Why?

> I would choose sha256_hash due to its high collision resistance. But 
> built_in_hash is a close second for its speed and having better security
> than the other options.

5. In your own words, explain each line in the pearson hash function above in terms of the criteria you listed in question 2.

> 1. "def pearson_hash(key: str, size: int) -> int:" - This line takes a key and the size of
> the table.  
>    1. This is in line with _Determinism_ as the same input will always give the same 
>    result.
>    2. This line takes no salt or secret key involved and has so this line offers no
>    additional _Security_.
> <br> <br>
> 
> 2. "hash_ = 0" - This line initialises the hash value. 
>    1. It's simple and _efficient_.
>    2. This affects _Sensitivity / Collision Resistance_ and could contribute to 
>    patterns that increase _collision risk_.
> <br> <br>
> 
> 3. "for char in key:
> hash_ = pearson_table[hash_ ^ ord(char)]" - This is the main loop that processes 
> the given key.
> 
>    1. Weak _security_ that lacks the necessary complexity to prevent attacks.
>    2. A single change in input typically leads to a completely different final hash, 
>    so it has a reasonably high _sensitivity_.
>    3. _Collision Resistance_ is moderate to low, different strings can easily 
>    end up with the same hash, especially for small size values.
>    4. Each iteration is fast, making this very _efficient_ even for long strings.
>    5. If the table is well shuffled the output could be fairly _Uniform_.
> <br> <br>
> 
> 4. "return hash_ % size" - Return hash.
>    1. _Uniformly_ Maps the 0–255 range down to the table's size. 
>    2. Reduces the number of possible outputs, increasing the chance of _collisions_.
>    3. Reduces hash space, which can make brute-force attacks easier weakening _security_.

6. Write pseudocode of how you would store Players in PlayerLists in a hash map.

> Your answer here

## Reflection

1. What was the most challenging aspect of this task?

> These questions. I genuinely found the researching and documenting
> the hardest part of this task. I prefer coding to documenting.

2. If you didn't have to use a PlayerList, how would you have changed the implementation of the hash map and why?

> I don't know, I guess I would make some other list function to
> substitute/replace PlayerList. I think the hashmap is fine as is.
> Though I might have decided to change my hash function, as after
> my research I believe sha256 may have been the better choice.

## Reference

### Key Dimensions of Hash Functions

1. **Uniformity**: the probability of any given hash value within the range of possible hash values should be approximately equal.

2. **Determinism**: a given input will always produce the same output.

3. **Efficiency**: the time complexity of computing the hash value should be constant, the hash function should be fast to compute, and utilize the architecture of the computer effectively

4. **Collision Resistance:** minimize the probability of collisions, through a variety of mechanisms.

5. **Sensitivity to input changes:** small changes in the input should produce large changes in the output.

6. **Security**
   - It should be computationally infeasible to find an input key that produces a specific hash value (non-reversibility)
   - The output hash values should appear random and unpredictable.
