n = int(input())

lis = list(map(int,input().strip().split()))

maxVal = max(lis)
while maxVal == max(lis):
    lis.remove(max(lis))
    
print(max(lis))