# 🪟 Sliding Window

> **Sliding window** processes a contiguous part of an array or string by moving a window instead of recalculating everything from scratch.

## 📌 Table of Contents
- [1. When to Use Sliding Window](#1-when-to-use-sliding-window)
- [2. Types of Sliding Window](#2-types-of-sliding-window)
- [3. Common Clues](#3-common-clues)
- [4. General Templates](#4-general-templates)
- [5. Example: Maximum Sum of K Consecutive Elements](#5-example-maximum-sum-of-k-consecutive-elements)
- [6. Complexity](#6-complexity)
- [7. Quick Checklist](#7-quick-checklist)
- [8. Python Tools to Remember](#8-python-tools-to-remember)

---

## 1. When to Use Sliding Window

Consider sliding window when a problem asks about a **contiguous subarray or substring** and you can update information efficiently as the window moves.

Examples:
- Maximum or minimum sum of a subarray of fixed length.
- Longest substring with no repeated characters.
- Smallest substring containing required characters.
- Count subarrays satisfying a condition, when the condition has the right properties.

## 2. Types of Sliding Window

### Fixed-size window

The window must contain exactly `k` elements or characters.

Typical clues:
- “Every subarray of size `k`”
- “Maximum average of `k` consecutive elements”
- “Find anagrams of a pattern” (often combined with frequency counts)

### Variable-size window

The window grows and shrinks to satisfy a condition.

Typical clues:
- “Longest substring with at most `k` distinct characters”
- “Smallest subarray with sum at least `target`” (for positive numbers)
- “Longest substring without repeating characters”

> **Important:** A standard variable-size sum window generally relies on non-negative or positive values. With arbitrary negative numbers, shrinking the left side may not behave predictably; prefix sums or another technique may be needed.

## 3. Common Clues

| Problem clue | Possible approach |
|---|---|
| Contiguous subarray or substring | Consider a window |
| Window has exactly `k` items | Fixed-size window |
| Longest valid substring/subarray | Expand right; shrink left when invalid |
| Smallest valid window | Expand until valid; shrink while it remains valid |
| Track character counts | Window + frequency map/array |
| Count valid windows ending at each position | Sometimes add `right - left + 1`, if all suffix windows in the current valid window qualify |

A sliding window is a **technique**, not a data structure. It is often combined with a hash map, set, counter array, or deque.

## 4. General Templates

### Fixed-size window

```python
left = 0
window_state = 0

for right in range(len(nums)):
    # Add nums[right] to the window state.

    if right - left + 1 > k:
        # Remove nums[left] from the window state.
        left += 1

    if right - left + 1 == k:
        # Update the answer using the current window.
        pass
```

### Variable-size window

```python
left = 0

for right in range(len(nums)):
    # Add nums[right] to the window state.

    while window_is_invalid:
        # Remove nums[left] from the window state.
        left += 1

    # Update the answer using the valid window.
```

The exact condition and state updates depend on the problem. Define what makes the window valid before using a template.

## 5. Example: Maximum Sum of K Consecutive Elements

Given `nums = [2, 1, 5, 1, 3, 2]` and `k = 3`, find the maximum sum of any three consecutive elements.

The window sums are `8`, `7`, `9`, and `6`, so the answer is `9`.

Instead of summing all `k` elements again for each window:
1. Calculate the first window's sum.
2. Add the new element when moving right.
3. Remove the element that leaves on the left.
4. Track the maximum sum.

```python
nums = [2, 1, 5, 1, 3, 2]
k = 3

window_sum = sum(nums[:k])
best = window_sum

for right in range(k, len(nums)):
    window_sum += nums[right] - nums[right - k]
    best = max(best, window_sum)

print(best)  # 9
```

## 6. Complexity

For the example above:
- **Time:** `O(n)` — each element enters and leaves the window at most once.
- **Auxiliary space:** `O(1)` — only a few variables are maintained.

For frequency-map windows, space depends on the number of distinct values or characters stored.

## 7. Quick Checklist

- [ ] Is the problem about a contiguous subarray or substring?
- [ ] Is the window fixed-size or variable-size?
- [ ] What information must be maintained?
- [ ] What makes the window valid or invalid?
- [ ] When should the left side move?
- [ ] Can I update state incrementally?

## 8. Python Tools to Remember

- `collections.Counter` — convenient frequency counts.
- `collections.defaultdict` — frequency maps without manual initialization.
- `collections.deque` — efficient operations at both ends; useful for a monotonic deque in window maximum/minimum problems.
- `itertools.pairwise()` — useful for adjacent pairs, but not a replacement for a general sliding-window algorithm.

**Remember:** Identify the window invariant first. Know what the window represents and exactly when to expand or shrink it.
