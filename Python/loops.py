if __name__ == '__main__':
    n = int(input())
 
count = 0
while (count <= n):
    print(count * count)
    count += 1
    if count == n:
        break