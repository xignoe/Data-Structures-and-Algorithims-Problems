def twoSum(arr, target):

    hashMap = {}
    for i, num in enumerate(arr):
        if target - num in hashMap:
            return[hashMap[target - num], i]

    return [-1, -1]

print(twoSum([2,7,11,15], 9))