def find_averages_of_subarrays(k, arr):
    resultArray = []

    windowSum = 0.0

    for i in range(k):
        windowSum += arr[i]
    
    resultArray.append(windowSum / k)

    for j in range(k, len(arr)):
        windowSum += arr[j]
        windowSum -= arr[(j - k)]
        resultArray.append((windowSum / k))    

    return resultArray
        
def main():
    print(find_averages_of_subarrays(5,[1,2,3,4,5,6,7,8]))

main()





    

    