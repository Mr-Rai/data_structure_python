# two sums
def two_sums(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        left_over = target - num
        if left_over in seen:
            return [seen[left_over], i]
        seen[num] = i
    return []


nums = [2, 7, 11, 15]
target = 26
print(two_sums(nums, target))

# First Non-Repeating Character
# Given a string, return the index of the first character that doesn't repeat. Return -1 if none.


def first_unique_char(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    for i, char in enumerate(s):
        if freq[char] == 1:
            return i, char
    return -1, "None"


print(first_unique_char("eetcode"))

# Merge Two Sorted Lists
# Given two sorted lists, merge them into one sorted list without using sorted().


def sorted_list(lst1, lst2):
    lst = lst1 + lst2
    for i in range(len(lst)):
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


print(sorted_list(lst1=[1, 3, 5], lst2=[2, 4, 6]))

#  Group Anagrams
# Given a list of strings, group the anagrams together.

from collections import defaultdict


def group_anagrams(arr):
    data = defaultdict(list)
    for word in arr:
        key = tuple(sorted(word))
        data[key].append(word)

    return list(data.values())


lst = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(arr=lst))

# Subarray Sum Equals K
# Given a list and integer k, return the count of subarrays that sum to k.


def subarray_sum(lst, k):
    seen = {}
    left = 0
    n = len(lst)
    for i in range(n):
        return


arr = [1, 2, 3]
k = 3
print(subarray_sum(arr, k))


# top k frequent element


def freq_elem(arr, k):
    freq = {}
    for elem in arr:
        freq[elem] = freq.get(elem, 0) + 1
    return [key for key, value in freq.items() if value >= k]


print(freq_elem(arr=[1, 1, 2, 2, 2, 3], k=2))
