#Difficulty: 1064
# Time: O(n), Space: O(1)

t = int(input())

for _ in range(t):
    x, y, z = map(int, input().split())
    if x >= y:
        print("PIZZA")
    elif x >= z:
        print("BURGER")
    else:
        print("NOTHING")
