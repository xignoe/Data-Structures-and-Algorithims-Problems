def removeDuplicates(arr):
    count = 1

    for i in range(len(arr) - 1):
        if (arr[i] != arr[i + 1]):
            arr[count] = arr[i + 1]
            count += 1


    return count
    
print(removeDuplicates([1,2,3,3,4]))
print(removeDuplicates([2,3,3,3,6,9,9]))
print(removeDuplicates([2,2,2,11]))