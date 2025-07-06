#Difficulty: 639
# Time: O(n), Space: O(1)

t = int(input())

for _ in range(t):
    x, y = map(int,input().split())
    print(abs(x-y))
