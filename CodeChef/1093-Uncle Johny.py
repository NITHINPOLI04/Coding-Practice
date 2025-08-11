#Difficulty: 1093
# Time: O(nlogn), Space: O(n)

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    k = int(input())
    
    target = a[k-1]
    sorted_a = sorted(a)
    
    for i in range(n):
        if sorted_a[i] == target:
            print(i+1)
            return

t = int(input())
for _ in range(t):
    solve()
