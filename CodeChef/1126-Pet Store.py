#Difficulty: 1126
# Time: O(1), Space: O(1)

def solve():
    n = int(input())
    animals = list(map(int, input().split()))

    counts = {}
    for animal in animals:
        counts[animal] = counts.get(animal, 0) + 1

    for count in counts.values():
        if count % 2 != 0:
            print("NO")
            return

    print("YES")

t = int(input())
for _ in range(t):
    solve()
