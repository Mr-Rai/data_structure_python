| # | Patterns                           | Core DS Used| Code File                              | Status |
|---|------------------------------------|-------------|----------------------------------------|--------|
| 1 | [Sliding Window](#sliding-window)  | list, deque |[Sliding Window](sliding_windows.py)    | ✅ |
| 2 | [Two Pointers](#two-pointers)      | list        |[Two Pointers](two_pointers.py)         | ✅ |
| 3 | [Monotonic Stack](#monotonic-stack)| stack (list)| [Monotonic Stack](monotonic_stack.py)  | ⌛ |
| 4 | [Monotonic Queue](#monotonic-queue)| deque       | [Monotonic Queue](monotonic_queue.py)  | ⌛ |
| 5 | [Prefix Sum](#prefix-sum)          | list, dict  | [Prefix Sum](prefix_sum.py)            | ⌛ |
| 6 | [Fast & Slow Pointers](#fast--slow-pointers)|linked list / list| [Fast & Slow Pointers](fast_and_slow_pointers.py) | ⌛ |
| 7 | [Binary Search on Answer](#binary-search-on-answer) | list | [Binary Search on Answer](binary_search_on_answer.py) | ⌛|


----------------

# Sliding Window
- The Core Idea you have an array. You need to find something about a contiguous subarray - max sum, longest substring,count of valid windows, etc.
- Brute force checks every possible subarray: $O(n^2)$. Sliding window does it in $O(n)$ by maintaining a window with two pointers and only updating what changed.
- The key insight: when you move the window one step right, you don't recompute from scratch. You add one element on the right and remove one on the left.

## Type 1: Fixed-Size Window
Window size k is given. Slide it across, track something. Problem: Maximum sum of any subarray of size k.

```python
def max_sum_fixed(arr, k):
    n = len(arr)
    if n < k:
        return None

    # Build the first window
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Slide: add right element, remove left element
    for i in range(k, n):
        window_sum += arr[i]  # add incoming
        window_sum -= arr[i - k]  # remove outgoing
        max_sum = max(max_sum, window_sum)

    return max_sum


arr = [2, 1, 5, 1, 3, 2]
k = 3
# windows: [2,1,5]=8, [1,5,1]=7, [5,1,3]=9, [1,3,2]=6
# answer: 9
```

## Type 2: Variable-Size Window
Window size is not fixed - you expand and shrink based on a condition. Template (memorize this):

```python
left = 0
state = {}  # or counter, or integer - tracks window contents

for right in range(len(arr)):
    # 1. Expand: add arr[right] to state

    # 2. Shrink: while window is invalid, remove arr[left] and left++
    while window_is_invalid:
        # remove arr[left] from state
        left += 1

    # 3. Window is now valid - update answer
    answer = max(answer, right - left + 1)
```

----------------------

# Two Pointers

Two pointers means maintaining two indices into an array and moving them based on a condition. Instead of checking every pair with nested loops - $O(n^2)$ - you eliminate large chunks of the search space with each move - $O(n)$.

**There are two variants:**
- Opposite ends - left starts at 0, right starts at end, they move toward each other
- Same direction - both start at 0, move forward at different speeds (this overlaps with sliding window)

## Variant 1: Opposite Ends
Problem: Two Sum on a Sorted Array. Array is sorted. Find two numbers that add to target.

```python
def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        current = nums[left] + nums[right]

        if current == target:
            return [left, right]
        elif current < target:
            left += 1       # need bigger sum, move left forward
        else:
            right -= 1      # need smaller sum, move right back

    return []

# [2, 7, 11, 15], target=9 → [0, 1]
```

**Why it works:** Array is sorted. If sum is too small, the only way to increase it is move left pointer right. If too big, move right pointer left. You never miss a valid pair.

> Time: $O(n)$. Space: $O(1)$.

## Variant 2: Same Direction
Problem: Remove Duplicates from Sorted Array (in-place)

```python
def remove_duplicates(nums):
    if not nums:
        return 0

    slow = 0   # points to last unique element written

    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:   # found a new unique element
            slow += 1
            nums[slow] = nums[fast]

    return slow + 1   # length of unique portion

# [1,1,2,3,3,4] → 4, nums becomes [1,2,3,4,...]
```

slow is the write pointer. fast scans ahead. When fast finds something new, slow advances and writes it.

> Time: $O(n)$. Space: $O(1)$.

------------------------

# Monotonic Queue

A monotonic queue is a deque where elements are maintained in increasing or decreasing order - same concept as monotonic stack, but you can remove from both ends. This makes it useful when you need the max or min of a sliding window efficiently.

**The key difference from monotonic stack:**
- Stack: only care about next/previous boundary
- Queue: care about max/min within a moving window of fixed size k

**Core insight:** For a window of size k, you don't need all k elements - you only need candidates that could be the maximum. Any element smaller than the current element will never be the maximum for any future window, so discard it immediately.

## Type 1: Sliding Window Maximum
Given a list and window size k, return the max of each sliding window.
```python
from collections import deque

def sliding_window_max(nums, k):
    result = []
    dq = deque()    # stores indices, values decrease front to back

    for i in range(len(nums)):
        # remove indices outside the current window
        if dq and dq[0] < i - k + 1:
            dq.popleft()

        # remove indices whose values are smaller than current
        # they can never be the max for any future window
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)

        if i >= k - 1:                      # window is full
            result.append(nums[dq[0]])      # front is always the max

    return result

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
# → [3, 3, 5, 5, 6, 7]
```

## Type 2: Sliding Window Minimum
Same idea, flip the comparison - maintain increasing order instead.
```python
from collections import deque

def sliding_window_min(nums, k):
    result = []
    dq = deque()    # stores indices, values increase front to back

    for i in range(len(nums)):
        if dq and dq[0] < i - k + 1:
            dq.popleft()

        while dq and nums[dq[-1]] > nums[i]:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(nums[dq[0]])      # front is always the min

    return result

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
# → [-1, -3, -3, -3, 3, 3]
```

## Monotonic Stack vs Monotonic Queue

| | Monotonic Stack | Monotonic Queue |
|---|---|---|
| DS used | list | deque |
| Remove from | top only | both ends |
| Solves | next/previous greater/smaller | sliding window max/min |
| Window | no fixed window | fixed size k |
| Complexity | O(n) | O(n) |

## Complexity
- **Time:** O(n) - each element added and removed at most once
- **Space:** O(k) - deque holds at most k elements

