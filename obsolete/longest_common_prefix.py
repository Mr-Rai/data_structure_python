class Solution:
    def longestCommonPrefix(self, strs):
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i >= j:
                    return ""

                print(strs[i], strs[j])


strs = ["flower", "flow", "flight"]
print(Solution().longestCommonPrefix(strs=strs))
