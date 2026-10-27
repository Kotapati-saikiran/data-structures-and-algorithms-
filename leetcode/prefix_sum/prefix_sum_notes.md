
## 1. What Is a Prefix Sum?

A **prefix sum** is the cumulative sum of elements from the beginning of an array up to a particular index.

For an array `nums`, define:

- `prefix_sum[i]` = sum of `nums[0]` through `nums[i]`.

Example:

```python
nums = [2, 3, 1, 5]
```

| Index | Element | Prefix sum |
|---:|---:|---:|
| 0 | 2 | 2 |
| 1 | 3 | 5 |
| 2 | 1 | 6 |
| 3 | 5 | 11 |

The running prefix sum can be updated in one pass:

```python
running_sum += nums[i]
```

### Prefix sum of a range

If `prefix_sum[i]` means the sum from index `0` through `i`, then the sum of a subarray from index `left` to `right` is:

- If `left == 0`: `prefix_sum[right]`
- Otherwise: `prefix_sum[right] - prefix_sum[left - 1]`

In formula form:

\[
\text{sum}(left,right)=P[right]-P[left-1]
\]

This works because subtracting the earlier prefix removes the elements before the subarray.

**Important:** Subtract prefix sums, not individual array elements.

---

## 2. When to Use Prefix Sum

Consider prefix sums when a problem asks you to:

- Calculate sums of many subarrays or ranges.
- Answer repeated range-sum queries efficiently.
- Count contiguous subarrays that satisfy a sum-related condition.
- Find subarrays with a target sum.
- Work with cumulative balances, running totals, or cumulative counts.
- Combine a running sum with a hashmap to remember earlier prefix sums or their remainders.

Prefix sums are particularly useful when repeatedly summing each subarray from scratch would be too slow.

### Prefix sum vs. sliding window

| Prefix sum | Sliding window |
|---|---|
| Uses cumulative sums to reason about ranges. | Maintains a current window using pointers. |
| Often works well with negative numbers. | Sum-based shrinking/expanding rules are easiest when numbers are non-negative and the condition behaves predictably. |
| Can be combined with a hashmap to count matching earlier prefix sums. | Often useful for contiguous windows with a condition that can be maintained as the window changes. |
| Useful for range queries and subarray counting. | Useful for fixed-size windows or suitable variable-size windows. |

**Do not choose sliding window just because the problem says “contiguous.”** Contiguity means the elements are adjacent; it does not automatically mean sliding window is the best technique.

---

## 3. Common Clues

Look for phrases such as:

- “Subarray sum”
- “Sum between index `left` and `right`”
- “Multiple range-sum queries”
- “Number of subarrays whose sum equals `k`”
- “Number of subarrays whose sum is divisible by `k`”
- “Longest subarray with a given sum”
- “Cumulative sum” or “running total”

These are clues, not guarantees. Check the constraints and the exact condition before choosing an approach.

### A useful question to ask

> Can I reuse information from earlier elements instead of recalculating the sum of every range?

If yes, prefix sums may help.

---

## 4. Time and Space Complexity

Let `n` be the length of the array.

| Operation | Time | Extra space |
|---|---:|---:|
| Build a prefix-sum array | `O(n)` | `O(n)` |
| Answer one range-sum query after preprocessing | `O(1)` | `O(1)` per query |
| Answer `q` range-sum queries after preprocessing | `O(n + q)` total | `O(n)` |
| Maintain only a running prefix sum | `O(n)` for one traversal | `O(1)` for the running sum |
| Prefix sum + hashmap | Usually `O(n)` expected time | Up to `O(n)` in general |

Hashmap operations such as lookup and insertion are `O(1)` on average, which is why prefix-sum/hashmap solutions are usually linear time.

---

## 5. Example: Build and Use Prefix Sums

Array:

```python
nums = [2, 3, 1, 5]
```

Prefix sums:

```text
Index:       0  1  2   3
nums:        2  3  1   5
prefix_sum:  2  5  6  11
```

Find the sum from index `1` through index `3`, which is the subarray `[3, 1, 5]`.

```text
prefix_sum[3] - prefix_sum[0]
= 11 - 2
= 9
```

Without prefix sums, we would add `3 + 1 + 5` directly. With prefix sums, the range sum is calculated by one subtraction.

---

## 6. Prefix Sum + Hashmap: Counting Subarrays

A prefix sum alone is not always enough to count subarrays efficiently. A hashmap can store information about earlier prefix sums.

### Example A: Count subarrays whose sum equals `target`

Let the current prefix sum be `P`. If an earlier prefix sum was `P - target`, then the elements between those two prefix positions sum to `target`.

The key idea is:

```text
needed_prefix_sum = current_prefix_sum - target
```

Store **frequencies** of earlier prefix sums, because the same prefix sum can occur multiple times and each occurrence may represent a different subarray.

### Example B: LeetCode 974 — Subarray Sums Divisible by K

For this problem, we want:

```text
subarray_sum % k == 0
```

If two prefix sums have the same remainder when divided by positive `k`, their difference is divisible by `k`.

For prefix sums `P1` and `P2`:

```text
P1 % k == P2 % k
```

Therefore:

```text
(P2 - P1) % k == 0
```

This means we can store the **frequency of each remainder**, rather than every prefix sum and its index.

Core reasoning for each element:

1. Add the element to the running prefix sum.
2. Calculate `remainder = prefix_sum % k`.
3. Add the previously seen frequency of that remainder to the answer.
4. Increase the frequency of the current remainder by one.

Initialize the remainder-frequency map with:

```python
remainder_frequency = {0: 1}
```

Why? It represents the empty prefix before the array begins. It allows a valid subarray starting at index `0` to be counted.

**Order matters:** Count the previous occurrences first, then record the current occurrence. This avoids counting an empty subarray.

### Negative numbers

In Python, `%` with a positive divisor returns a remainder from `0` through `k - 1`, even when the prefix sum is negative. This is convenient for grouping remainders.

---

## 7. Python Tools

### `dict`

A regular dictionary works well when you want to manage missing keys explicitly:

```python
if remainder in remainder_frequency:
    count += remainder_frequency[remainder]
    remainder_frequency[remainder] += 1
else:
    remainder_frequency[remainder] = 1
```

### `collections.defaultdict(int)`

`defaultdict(int)` supplies `0` for a missing key. This can simplify frequency counting:

```python
from collections import defaultdict

frequency = defaultdict(int)
frequency[0] = 1
```

Then a missing remainder has frequency `0` automatically. You still need to understand the algorithm; the library only simplifies dictionary bookkeeping.

### `collections.Counter`

`Counter` is useful for counting values in an existing iterable. For a prefix-sum algorithm that updates frequencies as it traverses the array, a normal dictionary or `defaultdict(int)` is often more natural.

### `itertools.accumulate`

`itertools.accumulate` can generate cumulative sums when you want the entire prefix-sum sequence:

```python
from itertools import accumulate

nums = [2, 3, 1, 5]
prefix_sums = list(accumulate(nums))
# [2, 5, 6, 11]
```

It is convenient for building prefix sums, but a running sum is often simpler when processing the array once.

---

## 8. Quick Checklist

Before implementing a prefix-sum problem, ask:

- [ ] Is the problem about a contiguous range or subarray?
- [ ] Do I need one range sum or many range sums?
- [ ] Can I reuse a cumulative sum rather than repeatedly summing elements?
- [ ] Do I need a prefix-sum array, or is one running sum enough?
- [ ] Am I counting subarrays? If so, could a hashmap help?
- [ ] Should the hashmap store prefix-sum values, remainders, or their frequencies?
- [ ] Do repeated prefix sums/remainders represent multiple different subarrays?
- [ ] Do I need an initial prefix sum of `0` to handle ranges starting at index `0`?
- [ ] Am I counting earlier prefixes before inserting the current prefix?
- [ ] Are negative values allowed, and does my approach handle them?
- [ ] Have I checked time and space complexity against the constraints?

---

## 9. Common Mistakes

1. **Confusing prefix sums with array elements.** Range sums use the difference between prefix sums, not the difference between individual elements.
2. **Checking only `prefix_sum % k == 0`.** For divisibility problems, valid subarrays can exist even when the current prefix sum itself is not divisible by `k`.
3. **Storing only whether a remainder exists.** Counting problems need the frequency, because several earlier prefixes may have the same remainder.
4. **Forgetting `{0: 1}`.** Without the initial zero remainder, subarrays beginning at index `0` can be missed.
5. **Updating frequency before counting.** This can count an empty subarray.
6. **Assuming every contiguous-subarray problem needs sliding window.** Negative numbers and the condition being checked can change which technique is appropriate.
7. **Assuming prefix sum always means an array.** You can store all prefix sums in an array, or keep only a running prefix sum when that is sufficient.

---

## 10. Final Mental Model

Think of a prefix sum as a **bookmark for the cumulative total** at each position.

- To get a range sum, subtract two bookmarks.
- To count subarrays, remember useful earlier bookmarks in a hashmap.
- For sums divisible by `k`, group bookmarks by their remainder.
- Store frequencies when multiple earlier bookmarks can create different valid subarrays.

The goal is not to memorize a template. It is to identify what information from the past can help you answer the question at the current index.
