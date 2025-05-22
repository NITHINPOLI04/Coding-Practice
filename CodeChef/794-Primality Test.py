#Difficulty: 794
# Time: O(sqrt(n), Space: O(1)

t = int(input())

for _ in range(t):
    n = int(input())
    flag = 0
    
    if n <= 1:
        flag = 1
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                flag = 1
                break
            
    if flag == 0:
        print('yes')
    else:
        print('no')
