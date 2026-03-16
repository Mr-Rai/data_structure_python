| # | Pattern                   | Core DS Used          | Difficulty    | Status    |
|---|---------------------------|-----------------------|---------------|-----------|
| 1 |Sliding Window             | list, deque           |Medium         | Pending   |
| 2 | Two Pointers              | list                  |Easy-Medium    | Pending   |
| 3 | Monotonic Stack           | stack (list)          | Medium-Hard   | Pending   |
| 4 | Monotonic Queue           | deque                 | Hard          | Pending   |
| 5 | Prefix Sum                | list, dict            | Medium        | Pending   |
| 6 | Fast & Slow Pointers      | linked list / list    | Medium        | Pending   |
| 7 | Binary Search on Answer   | list                  | Medium-Hard   | Pending   |

----------------

# Pattern 1: Sliding Window
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
Window size is not fixed — you expand and shrink based on a condition. Template (memorize this):

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