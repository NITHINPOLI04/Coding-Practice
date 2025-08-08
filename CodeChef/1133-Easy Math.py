#Difficulty: 1133

# cook your dish here
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    
    max_sum = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            product = a[i] * a[j]
            digit_sum = sum(int(digit) for digit in str(product))
            max_sum = max(max_sum, digit_sum)
            
    print(max_sum)
