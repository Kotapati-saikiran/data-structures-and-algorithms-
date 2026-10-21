# 👉👈 Two Pointers

> **Two pointers** uses two indices to explore a sequence efficiently, often avoiding nested loops.

## 📌 Table of Contents
- [1. When to Use Two Pointers](#1-when-to-use-two-pointers)
- [2. Common Patterns](#2-common-patterns)
- [3. Common Clues](#3-common-clues)
- [4. Example: Pair Sum in a Sorted Array](#4-example-pair-sum-in-a-sorted-array)
- [5. Complexity](#5-complexity)
- [6. Common Mistakes](#6-common-mistakes)
- [7. Python Tools to Remember](#7-python-tools-to-remember)

---

## 1. When to Use Two Pointers

Consider two pointers when a problem involves an array, string, linked list, or sequence and two positions can move according to a rule.

Two pointers are especially useful when:
- The array is sorted and you need a pair with a target sum.
- You need to compare values from opposite ends.
- You need to remove duplicates in-place from a sorted array.
- You need to partition or rearrange elements.
- You need to compare or merge two sequences.
- You need to check a palindrome.

## 2. Common Patterns

### Opposite-direction pointers

Start one pointer at the beginning and the other at the end. Move one or both based on a comparison.

Useful for:
- Pair sum in a sorted array.
- Palindrome checks.
- Container With Most Water.

### Same-direction pointers

Both pointers move forward, but at different rates or for different roles.

Useful for:
- Removing duplicates in-place.
- Fast and slow pointer problems.
- Partitioning elements.
- Some sliding-window problems.

### Two sequences

Use one pointer for each sequence.

Useful for:
- Merging sorted arrays.
- Comparing strings.
- Finding common elements in sorted sequences.

## 3. Common Clues

| Problem clue | Possible approach |
|---|---|
| Sorted array + pair sum | Start at both ends |
| Palindrome or symmetric comparison | Compare the left and right ends |
| Remove duplicates in-place | Slow pointer tracks the next write position |
| Two sorted arrays | Advance the pointer with the smaller current value |
| Cycle detection in a linked list | Fast and slow pointers |
| Need linear time instead of checking every pair | Look for a rule that safely moves one pointer |

Two pointers are a **technique**, not a data structure. The reason a pointer can move must come from the problem's properties.

## 4. Example: Pair Sum in a Sorted Array

Given `nums = [1, 2, 4, 6, 8, 9]` and `target = 10`, find two values whose sum equals the target.

1. Start `left` at the first element and `right` at the last.
2. Calculate `nums[left] + nums[right]`.
3. If the sum is too small, move `left` right to increase the sum.
4. If the sum is too large, move `right` left to decrease the sum.
5. Stop when the target is found or the pointers meet.

```python
def pair_sum(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        total = nums[left] + nums[right]

        if total == target:
            return [nums[left], nums[right]]
        elif total < target:
            left += 1
        else:
            right -= 1

    return []

print(pair_sum([1, 2, 4, 6, 8, 9], 10))  # [1, 9]
```

**Why does this work?** If the sum is too small, keeping the current left value and moving the right pointer left can only make the sum smaller or equal. So the left pointer must move forward. The opposite reasoning applies when the sum is too large.

The sorted order is essential to this elimination logic.

## 5. Complexity

For the pair-sum example:
- **Time:** `O(n)` — each pointer moves in only one direction.
- **Auxiliary space:** `O(1)` — only a few variables are used.

Some two-pointer problems require sorting first, which adds preprocessing time and may change the space complexity.

## 6. Common Mistakes

- Applying the opposite-direction pair-sum method to an unsorted array without a valid reason.
- Moving both pointers when only one should move.
- Forgetting to stop when pointers meet or cross.
- Confusing two pointers with sliding window. Sliding window is a related technique that maintains a contiguous range; not every two-pointer problem is a sliding window.
- Assuming every two-pointer solution is `O(n)` without accounting for sorting or other work.

## 7. Python Tools to Remember

- `enumerate()` — gives an index and value when scanning.
- `zip()` — iterates over sequences together.
- `itertools.pairwise()` — iterates over adjacent pairs; useful for neighboring comparisons, but not a general replacement for two pointers.

### Quick Checklist

- [ ] What does each pointer represent?
- [ ] Which condition tells me to move the left pointer?
- [ ] Which condition tells me to move the right pointer?
- [ ] What property makes the movement safe?
- [ ] Can each pointer move only a linear number of times?

**Remember:** Two pointers become powerful when you can explain why moving a pointer cannot discard a valid answer.
