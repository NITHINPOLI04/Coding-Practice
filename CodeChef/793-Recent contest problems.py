#Difficulty: 793
#Time: O(n), Space: O(1)

t = int(input())

for _ in range(t):
    n = int(input())
    s_count = 0
    l_count = 0
    
    arr = list(input().split())
    
    for i in arr:
        if i == 'START38':
            s_count += 1
        else:
            l_count += 1
            
    
    print(s_count, l_count)
