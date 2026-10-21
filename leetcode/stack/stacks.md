# 📚 Stack Data Structure

> A **stack** follows **LIFO**: Last In, First Out. The last element added is the first one removed.

## 📌 Table of Contents
- [1. What Is a Stack?](#1-what-is-a-stack)
- [2. When to Use a Stack](#2-when-to-use-a-stack)
- [3. Common Clues](#3-common-clues)
- [4. Time Complexity](#4-time-complexity)
- [5. Example: Valid Parentheses](#5-example-valid-parentheses)
- [6. Monotonic Stack](#6-monotonic-stack)
- [7. Python Implementation](#7-python-implementation)
- [8. Quick Checklist](#8-quick-checklist)

---

## 1. What Is a Stack?

A stack supports adding and removing elements from one end, called the **top**.

- **Push:** Add an element to the top.
- **Pop:** Remove the top element.
- **Peek/top:** Inspect the top element without removing it.

Think of a stack of plates: you usually add or remove a plate from the top.

## 2. When to Use a Stack

Look for problems involving:
- Matching brackets or nested structures.
- Reversing or processing items in last-in, first-out order.
- Undo operations, backtracking, or tracking previous states.
- Evaluating expressions or parsing syntax.
- Finding the next greater/smaller element with a **monotonic stack**.
- Processing nested function calls or depth-first traversal.

## 3. Common Clues

| Problem clue | Possible stack approach |
|---|---|
| Balanced parentheses or brackets | Push opening brackets; match when closing brackets appear |
| Next greater element | Often use a monotonic decreasing stack |
| Next smaller element | Often use a monotonic increasing stack |
| Nested or recently opened item | Keep the most recent unresolved item on top |
| Undo the most recent action | Store actions/states in a stack |
| Evaluate postfix expression | Push operands; pop when an operator appears |

A stack is a data structure. A **monotonic stack** is maintained in increasing or decreasing order to solve particular next-greater/next-smaller problems.

## 4. Time Complexity

| Operation | Typical time complexity |
|---|---:|
| Push | `O(1)` amortized |
| Pop | `O(1)` |
| Peek at top | `O(1)` |
| Search for an arbitrary element | `O(n)` |

## 5. Example: Valid Parentheses

Given `s = "([])"`, determine whether every opening bracket is closed by the correct type and in the correct order.

Approach:
1. Push each opening bracket.
2. When a closing bracket appears, the stack must not be empty.
3. Pop the most recent opening bracket and check that the types match.
4. At the end, the stack must be empty.

```python
def is_valid(s):
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}

    for char in s:
        if char in "([{":
            stack.append(char)
        else:
            if not stack or stack.pop() != pairs.get(char):
                return False

    return not stack

print(is_valid("([])"))  # True
print(is_valid("([)]"))  # False
```

**Why a stack?** The most recently opened bracket must be the first one closed. That is exactly LIFO behavior.

- **Time:** `O(n)`
- **Auxiliary space:** `O(n)` in the worst case.

## 6. Monotonic Stack

A monotonic stack maintains values in a chosen order.

- **Increasing stack:** Values are maintained in increasing order from bottom to top.
- **Decreasing stack:** Values are maintained in decreasing order from bottom to top.

In a next-greater-element problem, keep indices of elements whose next greater value has not been found. When a larger value arrives, it resolves smaller values at the top.

Each index is pushed and popped at most once, so many monotonic-stack solutions run in `O(n)` time. The exact order depends on the problem and the implementation.

## 7. Python Implementation

Python lists work well as stacks:

```python
stack = []

stack.append(10)  # Push
stack.append(20)
top = stack[-1]      # Peek: 20
value = stack.pop()  # Pop: 20
```

Use `append()` and `pop()` at the end of the list. Avoid `pop(0)` for a stack because removing the first list element takes `O(n)` time.

## 8. Quick Checklist

- [ ] Does the most recent unresolved item need to be handled first?
- [ ] Is the problem about nested brackets or structures?
- [ ] Are you looking for next greater/smaller elements?
- [ ] Can each item be pushed and popped at most once?
- [ ] Would a stack preserve the information needed to resolve earlier elements?

**Python tools to remember:** A list is usually enough for a stack. Use `collections.deque` when you need efficient operations at both ends.

**Remember:** A stack is useful when the order of resolution is the reverse of the order in which items are encountered.
