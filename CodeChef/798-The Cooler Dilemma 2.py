#Difficulty: 798
#Time: O(1), Space: O(1)

t = int(input())

for _ in range(t):
    x, y = map(int,input().split())

    months = (y - 1) // x
        
    print(months)
