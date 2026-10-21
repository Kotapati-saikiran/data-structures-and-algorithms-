# 🔎 Binary Search

> **Binary search** repeatedly halves a search space using an ordering property or a monotonic condition.

## 📌 Table of Contents
- [1. When to Use Binary Search](#1-when-to-use-binary-search)
- [2. Common Clues](#2-common-clues)
- [3. Classic Binary Search](#3-classic-binary-search)
- [4. Example: Find a Target](#4-example-find-a-target)
- [5. Binary Search on the Answer](#5-binary-search-on-the-answer)
- [6. Complexity](#6-complexity)
- [7. Common Mistakes](#7-common-mistakes)
- [8. Python Tools to Remember](#8-python-tools-to-remember)

---

## 1. When to Use Binary Search

Use binary search when the search space is ordered, or when a condition changes monotonically from false to true (or true to false).

Typical cases:
- Find a target in a sorted array.
- Find the first or last occurrence of a value.
- Find the first position satisfying a condition.
- Find the minimum feasible capacity, speed, or time when feasibility is monotonic.
- Search a rotated sorted array or another specially structured search space.

## 2. Common Clues

| Problem clue | What to consider |
|---|---|
| Sorted array | Compare the target with the middle element |
| First/last position or insertion point | Boundary-style binary search |
| “Minimum possible maximum” or “maximum possible minimum” | Binary search on the answer may apply |
| Feasibility becomes true after a threshold | Search for the first true condition |
| Huge numeric range with a monotonic feasibility check | Binary search over candidate answers |

**Important:** Binary search needs a reliable way to discard half the remaining candidates. A sorted array is one way to get that property, but not the only way.

## 3. Classic Binary Search

Maintain a search interval. Inspect its middle element and decide which half can still contain the target.

```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

This version assumes `nums` is sorted in ascending order and returns any matching index, or `-1` if the target is absent.

## 4. Example: Find a Target

```text
nums = [1, 3, 5, 7, 9, 11]
target = 7
```

1. Check the middle value, `5`.
2. Since `7 > 5`, discard the left half including `5`.
3. Check the middle of the remaining interval, `9`.
4. Since `7 < 9`, search the left part of that interval.
5. Find `7`.

Each comparison removes about half the remaining candidates.

## 5. Binary Search on the Answer

Sometimes the problem does not ask you to find a value in a sorted array. Instead, it asks for the **smallest or largest answer that satisfies a condition**.

For example, suppose `feasible(speed)` tells you whether a speed is enough to finish a task within a deadline. If feasibility is monotonic — every speed above a feasible speed is also feasible — you can binary-search for the smallest feasible speed.

1. Define the range of possible answers.
2. Write a correct feasibility check.
3. Confirm that feasibility is monotonic.
4. Binary-search for the required boundary (first true or last true).

Do not use binary search on the answer unless the feasibility condition really is monotonic.

## 6. Complexity

| Operation | Time complexity |
|---|---:|
| Binary search in a sorted array | `O(log n)` |
| Extra space, iterative version | `O(1)` |

If the input must first be sorted, include that preprocessing cost: comparison sorting generally takes `O(n log n)` time.

## 7. Common Mistakes

- Using binary search when the search space has no ordering or monotonic property.
- Updating boundaries incorrectly and causing an infinite loop.
- Mixing inclusive intervals (`left <= right`) with exclusive-interval logic.
- Forgetting that `mid` can equal a boundary.
- Using a feasibility condition that is not monotonic.
- Forgetting to handle the case where the target or feasible answer does not exist.

## 8. Python Tools to Remember

- `bisect_left(nums, x)` — finds the insertion position before existing equal values.
- `bisect_right(nums, x)` — finds the insertion position after existing equal values.
- The `bisect` module helps with insertion points and boundaries in sorted lists, but inserting into a Python list still takes `O(n)` time because elements may need to shift.

### Quick Checklist

- [ ] Is the input sorted or the condition monotonic?
- [ ] What exact interval am I searching?
- [ ] Which half can be safely discarded?
- [ ] Am I looking for any match, the first true, or the last true?
- [ ] Are the boundary updates consistent?

**Remember:** The key skill is proving that each step can safely discard half of the search space.
