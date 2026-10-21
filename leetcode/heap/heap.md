# 🧠 Heap Data Structure

> A **heap** is a tree-based data structure that helps us efficiently access and remove the element with the highest priority.

## 📌 Table of Contents

- [1. What Is a Heap?](#1-what-is-a-heap)
- [2. When Should We Use a Heap?](#2-when-should-we-use-a-heap)
- [3. Time Complexity](#3-time-complexity)
- [4. Example: Find the 3rd Largest Element](#4-example-find-the-3rd-largest-element)
- [5. Heap vs. Algorithmic Approach](#5-heap-vs-algorithmic-approach)
- [6. Python Implementation](#6-python-implementation)
- [7. Quick Decision Checklist](#7-quick-decision-checklist)

---

## 1. What Is a Heap?

A heap is commonly implemented using an array. It is especially useful when we need to retrieve the minimum or maximum element repeatedly without sorting the entire collection.

There are two main types of heaps:

- **Min-Heap:** The smallest element is always at the root.
- **Max-Heap:** The largest element is always at the root.

**Key idea:** A heap keeps the highest-priority element readily accessible. It does not keep all elements fully sorted.

## 2. When Should We Use a Heap?

Look for these clues when analyzing a problem:

| Problem clue | How a heap helps |
|---|---|
| **Top K largest or smallest** | Maintains the K best candidates without sorting everything. |
| **Kth largest or smallest** | Keeps track of the element at a particular rank. |
| **Repeatedly extract minimum or maximum** | Makes it efficient to retrieve and remove the current best element. |
| **Priority-based processing** | Processes tasks or events according to priority. |
| **Merge K sorted lists** | Efficiently selects the smallest current element across multiple lists. |
| **Running minimum or maximum** | Maintains a best candidate as elements arrive, especially in streaming problems. |

> **Key idea:** Consider a heap when you repeatedly need the best candidate (minimum or maximum), especially when the collection changes or you do not need to sort every element.

A heap is not automatically the best choice whenever a problem asks for a minimum or maximum. Consider how many queries you need to answer, whether the data changes, and whether sorting or another data structure would be simpler.

## 3. Time Complexity

Let `n` be the number of elements currently in the heap.

| Operation | Typical time complexity |
|---|---:|
| Access the root (minimum or maximum) | `O(1)` |
| Insert an element | `O(log n)` |
| Remove the root | `O(log n)` |
| Build a heap from an array | `O(n)` |
| Search for an arbitrary element | `O(n)` |

## 4. Example: Find the 3rd Largest Element

**Problem:** Given an array, find its 3rd largest element.

```text
nums = [3, 2, 1, 5, 6, 4]
k = 3

Answer: 4
```

### Approach: Min-Heap of Size K

Instead of sorting the entire array, maintain a min-heap containing only the `k` largest elements encountered so far.

1. Insert each element into the min-heap.
2. If the heap size exceeds `k`, remove the smallest element.
3. Continue until all elements have been processed.
4. The root of the heap is the Kth largest element.

For the example, the final heap contains the three largest elements: `4`, `5`, and `6`. Its root is `4`, which is the answer.

### Why Does This Work?

Whenever the heap contains more than `k` elements, removing the smallest discards an element that cannot belong to the `k` largest elements seen so far.

After processing the entire array, the heap retains the `k` largest elements. Its root is the smallest among them — the Kth largest overall.

**Complexity**

- **Time:** `O(n log k)`
- **Auxiliary space:** `O(k)`

Here, `n` is the number of input elements and `k` is the requested rank. The heap never needs to hold more than `k` elements.

## 5. Heap vs. Algorithmic Approach

A heap is a **data structure**, not a complete problem-solving algorithm.

The algorithm describes what we do with the heap, while the heap makes certain operations efficient.

For the Kth-largest-element problem:

- **Problem-solving pattern:** Maintain the Top K elements.
- **Data structure:** Min-heap of size `k`.
- **Heap's responsibility:** Efficiently remove the smallest element when the heap exceeds `k` elements.
- **Final result:** The root contains the Kth largest element.

The same data structure can support different algorithms depending on the problem.

## 6. Python Implementation

Python provides the [`heapq`](https://docs.python.org/3/library/heapq.html) module, which implements a min-heap.

```python
import heapq

nums = [3, 2, 1, 5, 6, 4]
k = 3

heap = []

for num in nums:
    heapq.heappush(heap, num)

    if len(heap) > k:
        heapq.heappop(heap)

print(heap[0])  # Output: 4
```

For this approach, we maintain a heap of at most `k` elements, giving an overall time complexity of `O(n log k)` and auxiliary space complexity of `O(k)`.

**Python note:** `heapq` is a min-heap by default. A max-heap can be implemented using negated values or, in supported Python versions, the max-heap functions provided by `heapq`.

## 7. Quick Decision Checklist

Before choosing a heap, ask yourself:

- [ ] Do I need the smallest or largest element repeatedly?
- [ ] Do I need the Kth largest/smallest element or the Top K elements?
- [ ] Does the problem require processing items by priority?
- [ ] Would maintaining a heap avoid repeatedly sorting the entire collection?
- [ ] Is a heap more suitable than sorting, a monotonic deque, or an ordered data structure for the required operations?

If the problem involves repeatedly selecting the minimum or maximum, or maintaining a limited set of top candidates, a heap is a strong candidate.

> **Remember:** Recognizing a heap is only the first step. You must also identify the algorithmic pattern — such as Top K, priority scheduling, or merging sorted lists — that determines how the heap should be used.
