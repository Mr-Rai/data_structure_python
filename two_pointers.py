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
    zero_count = 0
    filtered_list = []
    for i in range(len(nums)):
        if nums[i] == 0:
            zero_count += 1
            nums.
        else:
            filtered_list.append(nums[i])
    return filtered_list + [0] * zero_count


unfiltred_list = [0, 1, 0, 3, 12]
filtered_list = move_zeroes(nums=unfiltred_list)
print(id(unfiltred_list) is id(filtered_list))
