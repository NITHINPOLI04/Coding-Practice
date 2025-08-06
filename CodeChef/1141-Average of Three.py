#Difficulty: 1141
# Time: O(n), Space: O(1)

def solve():
    x = int(input())
    a1 = 1
    a2 = 2
    a3 = 3 * x - 3
    if a3 != a1 and a3 != a2 and 1 <= a3 <= 1000:
        print(a1, a2, a3)
    else:
        # If the above fails, use the symmetric approach, adjusting if needed.
        a1 = x - 1
        a2 = x
        a3 = x + 1
        
        if a1 < 1:
            a1 = 1
            a2 = x + 1 # shifting to the right since a1 is at minimum value
            a3 = 3*x - a1 - a2

        if a3 > 1000:
            a3 = 1000
            a2 = x -1 # shifting to the left since a3 is at maximum value
            a1 = 3*x - a2 - a3
        
        if a1 != a2 and a2 != a3 and a1 != a3 and 1 <= a1 <= 1000 and 1 <= a2 <= 1000 and 1 <= a3 <= 1000:
            print(a1, a2, a3)
        else:
          #If everything fails pick 3, 6, 3x-9. This will always work.
          a1 = 3
          a2 = 6
          a3 = 3*x - 9
          print(a1,a2,a3)


t = int(input())
for _ in range(t):
    solve()
