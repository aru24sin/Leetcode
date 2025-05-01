def removeDuplicates(nums):
    dups = []
    for i in nums:
        num = nums[i]
        if not (num in dups):
            dups.append(num)
            print(nums[i])

    k = len(dups)
    print(dups)
    return nums, k


nums = [1,1,2]
nums, k = removeDuplicates(nums)















