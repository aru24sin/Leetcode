def removeDuplicates(nums):
    last = None
    k = 0
    new = []
    for i in range(0, len(nums)):
        curr = nums[i]
        if curr != last:
            new.append(curr)
            last = curr
            k += 1
        else:
            continue
    
    nums = new
    print(nums)

    return k

nums = [1,1,2]
k = removeDuplicates(nums)
print(k)














