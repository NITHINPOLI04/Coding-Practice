#Difficulty: 790
# Time: O(n), Space: O(1)

# cook your dish here
t = int(input())
player1_score = 0
player2_score = 0
max_lead = 0
winner = 0

for _ in range(t):
    s, r = map(int, input().split())
    player1_score += s
    player2_score += r
    
    lead = player1_score - player2_score
    
    if abs(lead) > max_lead:
        max_lead = abs(lead)
        winner = 1 if lead > 0 else 2

print(winner, max_lead)
