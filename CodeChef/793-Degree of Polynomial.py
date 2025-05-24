#Difficulty: 793
# Time: O(n), Space: O(1)

# cook your dish here
t = int(input())

for _ in range(t):
    n = int(input())
    
    arr = list(map(int,input().split()))

    for i in range(n - 1, -1, -1):
        if arr[i] != 0:
            print(i)
            break
