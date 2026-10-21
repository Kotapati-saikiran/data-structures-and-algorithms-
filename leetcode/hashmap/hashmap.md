# 🗂️ Hash Map (Hash Table)

> A **hash map** stores key-value pairs and usually provides fast lookup, insertion, and deletion by key.

## 📌 Table of Contents
- [1. What Is a Hash Map?](#1-what-is-a-hash-map)
- [2. When to Use a Hash Map](#2-when-to-use-a-hash-map)
- [3. Common Clues](#3-common-clues)
- [4. Time Complexity](#4-time-complexity)
- [5. Example: Two Sum](#5-example-two-sum)
- [6. Frequency Counting](#6-frequency-counting)
- [7. Python Tools](#7-python-tools)
- [8. Quick Checklist](#8-quick-checklist)

---

## 1. What Is a Hash Map?

A hash map stores information as **key-value pairs**.

```python
counts = {
    "apple": 2,
    "banana": 3,
}
```

Here, each fruit is a key and its count is the value.

A hash map is useful when you need to find, update, or count information associated with a key without scanning the entire collection every time.

In Python, the built-in `dict` is a hash map.

## 2. When to Use a Hash Map

Look for problems involving:
- Counting the frequency of values or characters.
- Checking whether a value has been seen before.
- Finding pairs that meet a condition, such as Two Sum.
- Grouping items by a shared property.
- Mapping a value to an index or other information.
- Tracking state within a sliding window.
- Caching results to avoid repeated work.

## 3. Common Clues

| Problem clue | How a hash map helps |
|---|---|
| “How many times does each value appear?” | Store value → frequency |
| “Have we seen this before?” | Store seen values in a set or dictionary |
| “Find a matching complement” | Store value → index or count |
| “Group words by anagrams” | Map a canonical signature → group |
| “Longest substring with constraints” | Track character counts or last-seen indices |
| “Count pairs/subarrays with a target property” | Store previously seen prefix values or frequencies |

A hash map is often combined with another algorithmic pattern. For example, a sliding window may use a hash map to track character frequencies.

## 4. Time Complexity

Typical average-case complexity for Python dictionaries:

| Operation | Average time complexity |
|---|---:|
| Insert or update a key | `O(1)` |
| Look up a key | `O(1)` |
| Delete a key | `O(1)` |
| Iterate through all entries | `O(n)` |

These are average-case expectations. An individual operation can take `O(n)` in the worst case under unfavorable collision behavior.

## 5. Example: Two Sum

**Problem:** Given `nums = [2, 7, 11, 15]` and `target = 9`, return the indices of two values that add up to the target.

For each number `num`, calculate its complement:

`complement = target - num`

If that complement has already been seen, the pair is found.

```python
def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return []

print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
```

**Why does this work?** The dictionary lets us check whether the complement appeared earlier in average `O(1)` time. We avoid checking every pair with a nested loop.

- **Time:** `O(n)` average.
- **Auxiliary space:** `O(n)`.

## 6. Frequency Counting

A common hash-map pattern is counting occurrences.

```python
nums = [1, 2, 2, 3, 1, 2]

counts = {}

for num in nums:
    counts[num] = counts.get(num, 0) + 1

print(counts)  # {1: 2, 2: 3, 3: 1}
```

The expression `counts.get(num, 0)` returns the existing count or `0` if the key is not present.

## 7. Python Tools

```python
from collections import Counter, defaultdict

nums = [1, 2, 2, 3, 1, 2]

counts = Counter(nums)  # Count occurrences

groups = defaultdict(list)  # Create missing values automatically
groups["even"].append(2)

print(counts[2])       # 3
print(groups["even"])  # [2]
```

- **`dict`** — general key-value mapping.
- **`collections.Counter`** — frequency counting.
- **`collections.defaultdict`** — convenient when building groups or accumulating values.
- **`set`** — use when you only need membership, not associated values.

## 8. Quick Checklist

- [ ] Do I need fast lookup by a value or key?
- [ ] Do I need to count occurrences?
- [ ] Do I need to remember an index or previous state?
- [ ] Can a dictionary replace a repeated linear search?
- [ ] Would a set be enough if I only care whether an item exists?
- [ ] Is this hash map supporting another pattern, such as sliding window or prefix sum?

**Remember:** Use a hash map when you need to remember information and retrieve it efficiently. First decide what the key represents and what value you need to store.
