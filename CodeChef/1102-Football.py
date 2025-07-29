#Difficulty: 1102
# Time: O(1), Space: O(1)

t= int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    
    result = []
    
    for i in range(n):
        each_score = (a[i] * 20) - (b[i] * 10)
        result.append(each_score)
        
    print(max(result)) if max(result) > 0 else print(0)
