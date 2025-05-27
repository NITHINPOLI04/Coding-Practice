#Difficulty: 786
# Time: O(nlogn), Space: O(1)

#Approach 1
t = int(input())

for _ in range(t):
    n, a, b = map(int,input().split())
    time = 0
    
    while(n/2 != 1):
        time = time + a + b
        n = n/2
    
    total_time = a + time
    
    print(total_time)

#----------------------------------------------
#Approach 2
# Time: O(n), Space: O(1)
import math

t = int(input())

for _ in range(t):
    n, a, b = map(int, input().split())

    num_rounds = int(math.log2(n))
    total_time = a * num_rounds + b * (num_rounds - 1)
    print(total_time)
