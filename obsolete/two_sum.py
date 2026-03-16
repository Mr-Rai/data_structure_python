def two_sum(lst, sum):
    seen = {}
    for i, num in enumerate(lst):
        print(i, num, sum - num)
        req = sum - num
        if req in seen:
            return [seen[req], i]
        seen[num] = i


# print(two_sum([2, 7, 11, 15], 17))


def longest_substring(s):
    return s


# print(longest_substring("abcabsdd"))
# print([0] * 3)

string = 1422559988


def sum_of_even_consecutive_digits(num):
    num_filtered = ""
    num = str(num)
    for i in range(len(str(num))):
        if int(num[i]) % 2 == 0:
            num_filtered += num[i]
        else:
            num_filtered += ","
    print(sum([int(digit) for digit in num_filtered.split(",") if digit]))


sum_of_even_consecutive_digits(string)


def reverse_list(lst):
    rev_lst = []
    for item in lst:
        rev_lst = [item] + rev_lst
    return rev_lst


rev_lst = reverse_list([2, 3, 4, 5])
print(rev_lst)
