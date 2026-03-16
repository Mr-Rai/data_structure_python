class Solution:
    def find_palidrome(self, num):
        return str(num) == "".join(list(str(num))[::-1])


res = Solution().find_palidrome(121)
print(res)
