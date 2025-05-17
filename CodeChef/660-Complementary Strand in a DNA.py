#Difficulty: 660
# Time: O(n), Space: O(1)

t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    result = []
    
    for i in s:
        if i == 'A':
            result.append('T')
        elif i == 'T':
            result.append('A')
        elif i == 'C':
            result.append('G')
        else:
            result.append('C')
            
    print(''.join(result))
