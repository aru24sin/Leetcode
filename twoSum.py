class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hmap = {} #make dictionary to store number as key and index as value
        for i,n in enumerate(nums): #enumerate list to get each index and number assigned to a local variable
            comp = target - n #calculate the complement to check if it is within the list
            if comp in hmap:
                return [hmap[comp], i] #return [index of comp in dict, index of curr num being checked]
            hmap[n] = i #append number as key and index as value in the dict
        return [] #if nothing is found return an empty list

nums = [2,7,11,15]
target = 9
print(Solution().twoSum(nums, target))