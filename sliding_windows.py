# Problem: Longest substring without repeating characters.


def longest_unique_substring(s):
    left = 0
    seen = {}
    max_len = 0

    for right in range(len(s)):
        char = s[right]
        if char in seen and seen[char] >= left:
            left = seen[char] + 1
        seen[char] = right
        print(f"{left=}, {seen=}, {right=}")
    return None


s = "abcabcbb"
print(longest_unique_substring(s))
