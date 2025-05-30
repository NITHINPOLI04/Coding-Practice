#Difficulty: 777
# Time: O(n), Space: O(1)

t = int(input())

for _ in range(t):
    H, X, Y = map(int,input().split())
    
    rem_H = H - Y
    count = 1
    while(rem_H > 0):
        rem_H -= X
        count += 1
    print(count)
