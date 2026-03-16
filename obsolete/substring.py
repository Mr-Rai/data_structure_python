def longest_substring(string):
    right = 0
    left = 0
    seen = set()
    for right in range(len(string) - 1):
        if string[right] != string[right + 1]:
            right += 1
            seen.add(string[right])
        else:
            left = right

    return string[left : right - left + 1]
    return string


print(longest_substring("abcabcde"))
