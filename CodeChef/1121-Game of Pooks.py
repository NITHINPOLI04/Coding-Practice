#Difficulty: 1121
# Time: O(1), Space: O(1)

def solve():
    n = int(input())
    if n == 1:
        print(1)
    elif n == 2:
        print(1)
    elif n == 3:
        print(2)
    else:
        print(n)

t = int(input())
for _ in range(t):
    solve()
