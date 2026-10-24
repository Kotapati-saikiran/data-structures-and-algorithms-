import heapq
from collections import Counter

def medianSlidingWindow(nums, k):
    # small: max-heap for the smaller half.
    # Python has a min-heap, so store negative values.
    small = []

    # large: min-heap for the larger half.
    # Store values normally.
    large = []

    # Counts values that have left the window but may
    # still physically exist inside either heap.
    delayed = Counter()

    # Logical sizes count only VALID elements.
    # They are not necessarily equal to len(small/large),
    # because heaps can contain expired elements.
    small_size = 0
    large_size = 0

    result = []
    n = len(nums)

    # -------------------------------------------------
    # 1. LAZY DELETION: remove expired values from top
    # -------------------------------------------------
    def prune(heap, is_small):
        while heap:
            # Convert negative heap values back to actual
            # values when examining the max-heap.
            value = -heap[0] if is_small else heap[0]

            # If this value has an expired occurrence,
            # remove the top and consume one deletion mark.
            if delayed[value] > 0:
                heapq.heappop(heap)
                delayed[value] -= 1

                # Keep the Counter clean.
                if delayed[value] == 0:
                    del delayed[value]
            else:
                # The top is valid, so stop pruning.
                break

    # -------------------------------------------------
    # 2. REBALANCE: keep the two halves correctly sized
    # -------------------------------------------------
    def rebalance():
        nonlocal small_size, large_size

        # Make sure heap tops are valid before moving them.
        prune(small, True)
        prune(large, False)

        # small may contain at most one extra valid value.
        while small_size > large_size + 1:
            prune(small, True)

            # Remove the largest value from small.
            # Negate it back to its original value.
            value = -heapq.heappop(small)

            # Move that value into the normal min-heap.
            heapq.heappush(large, value)

            small_size -= 1
            large_size += 1

            prune(small, True)

        # If large has more values, move its smallest
        # valid value into small.
        while small_size < large_size:
            prune(large, False)

            value = heapq.heappop(large)

            # small stores negative values.
            heapq.heappush(small, -value)

            large_size -= 1
            small_size += 1

            prune(large, False)

    # -------------------------------------------------
    # 3. ADD: insert an incoming number
    # -------------------------------------------------
    def add_num(num):
        nonlocal small_size, large_size

        # Ensure the boundary used below is valid.
        prune(small, True)

        # If small is empty, or num belongs to the
        # smaller half, insert it into small.
        if not small or num <= -small[0]:
            heapq.heappush(small, -num)
            small_size += 1
        else:
            # Otherwise, it belongs in the larger half.
            heapq.heappush(large, num)
            large_size += 1

        # Restore the size balance.
        rebalance()

    # -------------------------------------------------
    # 4. REMOVE: mark an outgoing number as expired
    # -------------------------------------------------
    def remove_num(num):
        nonlocal small_size, large_size

        # Clean both boundaries before classifying num.
        prune(small, True)
        prune(large, False)

        # Mark one occurrence for lazy deletion.
        # It may remain buried in a heap for now.
        delayed[num] += 1

        # The largest value in small is the boundary.
        if num <= -small[0]:
            small_size -= 1

            # If the outgoing value is at the top,
            # remove it immediately.
            if num == -small[0]:
                prune(small, True)
        else:
            large_size -= 1

            # Likewise, remove it immediately if it is
            # currently the top of large.
            if large and num == large[0]:
                prune(large, False)

        # Restore balance after the logical removal.
        rebalance()

    # -------------------------------------------------
    # 5. SLIDING WINDOW
    # -------------------------------------------------
    for right, num in enumerate(nums):

        # Add the incoming element.
        add_num(num)

        # Once right reaches k, the element at right-k
        # is outside the current window.
        if right >= k:
            remove_num(nums[right - k])

        # A complete window first exists at index k-1.
        if right >= k - 1:

            # Never read an expired heap top as a median.
            prune(small, True)
            prune(large, False)

            if k % 2 == 1:
                # Odd window: middle value is the top
                # of the smaller half.
                result.append(float(-small[0]))
            else:
                # Even window: average the two middle values.
                result.append((-small[0] + large[0]) / 2.0)

        # -------------------------------------------------
        # 6. CONTROL SPACE: periodically rebuild heaps(Optional it for memory optimization)
        # -------------------------------------------------
        # Lazy deletion can leave expired values buried
        # inside heaps. Rebuild when physical heap storage
        # grows beyond 2*k elements.
        if len(small) + len(large) > 2 * k:

            # Extract the actual current window.
            start = max(0, right - k + 1)
            window = nums[start:right + 1]

            # Discard old heap entries and deletion marks.
            small.clear()
            large.clear()
            delayed.clear()

            small_size = 0
            large_size = 0

            # Rebuild using only the current window values.
            for x in window:
                if not small or x <= -small[0]:
                    heapq.heappush(small, -x)
                    small_size += 1
                else:
                    heapq.heappush(large, x)
                    large_size += 1

                # Keep the size invariant while rebuilding.
                if small_size > large_size + 1:
                    value = -heapq.heappop(small)
                    heapq.heappush(large, value)
                    small_size -= 1
                    large_size += 1
                elif small_size < large_size:
                    value = heapq.heappop(large)
                    heapq.heappush(small, -value)
                    large_size -= 1
                    small_size += 1

    return result


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(medianSlidingWindow(nums, k))
# [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]