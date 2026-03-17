| # | Patterns                           | Core DS Used                 | Difficulty    | Status |
|---|------------------------------------|------------------------------|---------------|--------|
| 1 | [Sliding Window](#sliding-window)  | list, deque                  |Medium         | ✅    |
| 2 | [Two Pointers](#two-pointers)      | list                         |Easy-Medium    | ⌛    |
| 3 | [Monotonic Stack](#monotonic-stack)| stack (list)                 | Medium-Hard   | ⌛    |
| 4 | [Monotonic Queue](#monotonic-queue)| deque                        | Hard          | ⌛    |
| 5 | [Prefix Sum](#prefix-sum)          | list, dict                   | Medium        | ⌛    |
| 6 | [Fast & Slow Pointers](#fast--slow-pointers) | linked list / list | Medium        | ⌛    |
| 7 | [Binary Search on Answer](#binary-search-on-answer) | list        | Medium-Hard   | ⌛    |

----------------

# Sliding Window
- The Core Idea you have an array. You need to find something about a contiguous subarray - max sum, longest substring,count of valid windows, etc.
- Brute force checks every possible subarray: O(n²). Sliding window does it in O(n) by maintaining a window with two pointers and only updating what changed.
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

Two pointers means maintaining two indices into an array and moving them based on a condition. Instead of checking every pair with nested loops - O(n²) - you eliminate large chunks of the search space with each move - O(n).

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

**Why it works:** Array is sorted. If sum is too small, the only way to increase it is move left pointer right. If too big, move right pointer left. You never miss a valid pair.<br>
**Time:** O(n). Space: O(1).

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

slow is the write pointer. fast scans ahead. When fast finds something new, slow advances and writes it.<br>
**Time:** O(n). Space: O(1).