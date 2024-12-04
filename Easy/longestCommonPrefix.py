class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans = ""
        strs = sorted(strs)
        first = strs[0]
        last = strs[-1]
        for i in range(min(len(first), len(last))):
            if (first[i] != last[i]):
                return ans
            ans += first[i]
        return ans

#test input to test function
ans = Solution().longestCommonPrefix(["flower", "flow", "flight"])
print(ans)

"""
This is a perfect simple example of using two pointers I believe. I have seen this pattern before
Where you traverse through the list in a similar elementary method as determining the median from 
a list of numbers in a list. There was no need for using a dictionary or nested loops as I 
believed.
"""