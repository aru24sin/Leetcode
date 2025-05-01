def removeDuplicates(nums):
    j = 0
    for i in range(1, len(nums)):
        if nums[j] != nums[i]:
            j += 1
            nums[j] = nums[i]
    print(nums)
    return j + 1

nums = [0,0,1,1,1,2,2,3,3,4]
k = removeDuplicates(nums)
print(k)