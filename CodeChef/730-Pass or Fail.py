#Difficulty: 730
# Time: O(1), Space: O(1)

t = int(input())

for _ in range(t):
    n, x, p = map(int,input().split())
    
    total_marks = (x * 3) - (n - x)
    
    if total_marks >= p:
        print("PASS")
    else:
        print("FAIL")
