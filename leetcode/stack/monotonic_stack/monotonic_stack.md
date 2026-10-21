# 📈 Monotonic Stack

> A **monotonic stack** is a stack that maintains its elements in a consistent increasing or decreasing order. It helps solve problems involving the next greater or smaller element efficiently.

## 📌 Table of Contents

- [1. What Is a Monotonic Stack?](#1-what-is-a-monotonic-stack)
- [2. When Should We Use It?](#2-when-should-we-use-it)
- [3. Increasing vs. Decreasing Stack](#3-increasing-vs-decreasing-stack)
- [4. Common Problem Clues](#4-common-problem-clues)
- [5. Example: Next Greater Element](#5-example-next-greater-element)
- [6. Python Implementation](#6-python-implementation)
- [7. Time and Space Complexity](#7-time-and-space-complexity)
- [8. Common Mistakes](#8-common-mistakes)
- [9. Quick Decision Checklist](#9-quick-decision-checklist)
- [10. Python Tools to Remember](#10-python-tools-to-remember)

---

## 1. What Is a Monotonic Stack?

A normal stack follows **LIFO** (Last In, First Out). A monotonic stack adds another rule: values represented in the stack must stay in a chosen order.

There are two common forms:

- **Monotonically increasing stack:** Values increase from the bottom of the stack to the top.
- **Monotonically decreasing stack:** Values decrease from the bottom of the stack to the top.

When a new element breaks the chosen order, we pop elements until the order is restored. Those popped elements may have just found their answer.

**Important:** Many solutions store **indices**, rather than values, so they can look up the original values and calculate distances.

## 2. When Should We Use It?

Consider a monotonic stack when a problem asks you to find the next or previous element that is:

- Greater than the current element.
- Smaller than the current element.
- Greater than or equal to the current element.
- Smaller than or equal to the current element.

It is also useful in problems that ask for:
- How many consecutive elements are visible before a taller or shorter element blocks the view.
- The largest rectangle in a histogram.
- The maximum area formed by bars or boundaries.
- The sum of subarray minimums or maximums.

The key pattern is that elements remain **unresolved** until a later element gives them the answer.

## 3. Increasing vs. Decreasing Stack

The exact stack order depends on the problem and on whether you are scanning from left to right or right to left. A common left-to-right setup is:

| Goal | Common stack behavior while scanning left to right |
|---|---|
| Next greater element | Keep a decreasing stack; pop while the current value is greater than the top value |
| Next smaller element | Keep an increasing stack; pop while the current value is smaller than the top value |

For “greater than or equal to” or “smaller than or equal to” problems, the comparison may need `>=` or `<=` instead of `>` or `<`.

**Do not memorize only the stack name.** Decide what condition makes the current element resolve the elements at the top.

## 4. Common Problem Clues

| Problem wording | Pattern to consider |
|---|---|
| Next greater element | Monotonic decreasing stack |
| Next smaller element | Monotonic increasing stack |
| Previous greater/smaller element | Monotonic stack, often scanning left to right |
| Daily temperatures / days until warmer weather | Next greater element using indices |
| Stock span | Previous greater element |
| Largest rectangle in a histogram | Increasing stack of indices |
| Sum of subarray minimums | Monotonic stack with carefully handled duplicate values |

A monotonic stack is a **technique built on a stack**, not a separate underlying data structure.

## 5. Example: Next Greater Element

**Problem:** For each element, find the first greater element to its right. If no greater element exists, return `-1`.

```text
nums   = [2, 1, 2, 4, 3]
answer = [4, 2, 4, -1, -1]
```

### How the approach works

Scan from left to right and keep indices of elements whose next greater element has not been found.

1. For each new value, compare it with the value at the top index of the stack.
2. While the current value is greater, pop that index: the current value is its next greater element.
3. Push the current index because its next greater element may appear later.
4. Any indices left in the stack at the end have no greater element to their right, so their answers stay `-1`.

### Walkthrough

For `nums = [2, 1, 2, 4, 3]`:

- `2`: no unresolved values to pop; push its index.
- `1`: it is not greater than `2`; push its index.
- `2`: it resolves `1`, because `2 > 1`. It does not resolve the earlier `2`, because the values are equal. Push its index.
- `4`: it resolves both pending `2` values; push its index.
- `3`: it is not greater than `4`; push its index.
- At the end, the unresolved values have answer `-1`.

## 6. Python Implementation

```python
def next_greater_elements(nums):
    n = len(nums)
    answer = [-1] * n
    stack = []  # Store indices with unresolved next-greater values

    for i, num in enumerate(nums):
        while stack and nums[stack[-1]] < num:
            index = stack.pop()
            answer[index] = num

        stack.append(i)

    return answer


nums = [2, 1, 2, 4, 3]
print(next_greater_elements(nums))  # [4, 2, 4, -1, -1]
```

The comparison uses `<` because the problem asks for a **strictly greater** element. If equal values should also count, the condition would need to change.

## 7. Time and Space Complexity

For the next-greater-element algorithm:

- **Time:** `O(n)` — each index is pushed once and popped at most once.
- **Auxiliary space:** `O(n)` — the stack and answer array can each hold up to `n` elements.

Although there is a `while` loop inside the `for` loop, the total work is linear because an index cannot be pushed or popped repeatedly without limit.

## 8. Common Mistakes

- **Choosing the wrong comparison:** `>` and `>=` solve different versions of a problem.
- **Storing values instead of indices:** Values alone may not provide the position or distance required by the question.
- **Forgetting unresolved elements:** Initialize answers appropriately, often to `-1`.
- **Assuming duplicates are irrelevant:** Equal values matter in many problems, especially subarray minimum/maximum sums.
- **Misidentifying the stack order:** State clearly whether the stack is increasing or decreasing from bottom to top.
- **Thinking nested loops always mean `O(n²)`:** In a monotonic stack, each element is usually pushed and popped at most once, giving `O(n)` total time.

## 9. Quick Decision Checklist

- [ ] Does the problem ask for a next or previous greater/smaller element?
- [ ] Does each element wait for a later element to resolve it?
- [ ] Can resolved elements be removed permanently from consideration?
- [ ] Should I store indices to calculate distances or refer back to values?
- [ ] Should equal values be popped too, or only strictly greater/smaller values?
- [ ] Can each index be pushed and popped at most once?

**Remember:** The core idea is to keep unresolved candidates in a stack. When a new element resolves the top candidate, pop it and record the answer.

## 10. Python Tools to Remember

- A Python `list` works well as a stack using `append()` and `pop()`.
- `enumerate(nums)` conveniently provides both the index and value.
- `collections.deque` is useful when you need efficient operations at both ends, but a standard monotonic stack usually only needs a list.

