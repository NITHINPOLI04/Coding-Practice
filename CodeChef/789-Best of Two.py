#Difficulty: 789
# Time: O(n), Space: O(1)

#Approach 1
t = int(input())

for _ in range(t):
    a1, a2, a3, b1, b2, b3 = map(int,input().split())
    
    a = [a1, a2, a3]
    b = [b1, b2, b3]
    
    a.sort(reverse = True)
    b.sort(reverse = True)
    
    if (a[0] + a[1]) > (b[0] + b[1]):
        print("Alice")
    elif (a[0] + a[1]) < (b[0] + b[1]):
        print("Bob")
    else:
        print("Tie")

#--------------------------------------------------------------

#Approach 2
t = int(input())

for _ in range(t):
    a1, a2, a3, b1, b2, b3 = map(int,input().split())
    
    alice_score = sum([a1, a2, a3]) - min(a1, a2, a3)
    bob_score = sum([b1, b2, b3]) - min(b1, b2, b3)

    if alice_score > bob_score:
        print("Alice")
    elif alice_score < bob_score:
        print("Bob")
    else:
        print("Tie")
