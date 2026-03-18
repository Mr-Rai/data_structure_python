def two_sums_sorted(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        curr_sum = nums[left] + nums[right]
        if curr_sum == target:
            return [left, right]
        elif curr_sum < target:
            print()
            left += 1
        else:
            right -= 1
    return []


print(two_sums_sorted(nums=[2, 7, 11, 15], target=13))

# Problem: Container With Most Water
# Given heights, find two lines that together with x-axis forms a container holding the most water.


def max_water(heights):
    left, right = 0, len(heights) - 1
    max_area = 0

    while left < right:
        width = right - left
        area = width * min(heights[left], heights[right])
        max_area = max(max_area, area)
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return max_area


print(max_water(heights=[1, 8, 6, 2, 5, 4, 8, 3, 7]))


# Problem: Three Sum
# Find all unique triplets that sum to zero.


def three_sums(nums):
    res = []
    nums.sort()
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            while left < right and nums[left] == nums[left + 1]:
                left += 1
            while left < right and nums[right] == nums[right - 1]:
                right -= 1
            if total == 0:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return res


print(three_sums(nums=[-1, 0, 1, 2, -1, -4]))  # expected [[-1,-1,2], [-1,0,1]]


# ----------- Variant 2: Same Direction -----------------#

# Problem: Problem: Move Zeroes to End


def move_zeroes(nums: list) -> list:
    """
    This is actually wrong because it creates a new list instead of
    modifying the original one in place, but it is still a valid
    solution to the problem.
    """
    zero_count = 0
    filtered_list = []
    for i in range(len(nums)):
        if nums[i] == 0:
            zero_count += 1
        else:
            filtered_list.append(nums[i])
    return filtered_list + [0] * zero_count


def move_zeroes_in_place(nums: list) -> list:
    """
    This is the correct solution to the problem, it modifies the original
    list in place.
    """
    zero_pos = 0
    # move items left where there is zero
    for next_point in range(len(nums)):
        if nums[next_point] != 0:
            nums[zero_pos] = nums[next_point]
            zero_pos += 1
    # replace all the items from zero_pos to end with zero
    while zero_pos < len(nums):
        nums[zero_pos] = 0
        zero_pos += 1
    return nums


unfiltred_list = [0, 1, 0, 3, 12]
filtered_list_invalid = move_zeroes(nums=unfiltred_list)
filtered_list_valid = move_zeroes_in_place(nums=unfiltred_list)
print(
    f"returned list memory address in {move_zeroes.__name__}: {id(unfiltred_list) == id(filtered_list_invalid)}"
)
print(
    f"returned list memory address in {move_zeroes_in_place.__name__}: {id(unfiltred_list) == id(filtered_list_valid)}"
)

# -------------------------------


def is_palindrome(s: str) -> bool:
    s_cleaned = "".join(char.lower() for char in s if char.isalnum())
    return s_cleaned == s_cleaned[::-1]


st = "A man, a plan, a canal: Panama"
print(is_palindrome(s=st))


def is_palindrome_twopointer(s: str) -> bool:
    s = "".join(c.lower() for c in s if c.isalnum())
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


import timeit

# using cpython slice [::-1] (It runs code in C language which is must faster)
t1 = timeit.timeit(lambda: is_palindrome(st * 100), number=10000)

# using while loop
t2 = timeit.timeit(lambda: is_palindrome_twopointer(st * 100), number=10000)

print(f"Slice: {t1:.3f}s")
print(f"Two pointer: {t2:.3f}s")
print(f"Slice is: {(t1/t2)*100} % Faster")
