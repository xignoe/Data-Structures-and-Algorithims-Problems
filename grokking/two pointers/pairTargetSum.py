def pairTargetSum(nums, target):
    l = 0
    r = len(nums) -1

    while (l < r):
        sumNums = nums[l] + nums[r]
        if target == sumNums:
            return [l, r]

        if sumNums < target:
            l += 1
        else: 
            r -= 1

    return [-1, -1]

print(pairTargetSum([2,3,4], 6))