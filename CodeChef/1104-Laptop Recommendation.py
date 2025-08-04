#Difficulty: 1104
# Time: O(n), Space: O(1)

# cook your dish here
t = int(input())

for _ in range(t):
    n = int(input())
    a = map(int,input().split())
    
    result = {}
    for laptop in a:
        if laptop in result:
            result[laptop] += 1
        else:
            result[laptop] = 1

    max_freq = 0
    max_laptop = -1
    count = 0

    # Find the laptop(s) with the maximum frequency
    for laptop, freq in result.items():
        if freq > max_freq:
            max_freq = freq
            max_laptop = laptop
            count = 1  # Reset count when a new maximum is found
        elif freq == max_freq:
            count += 1  # Increment count if another laptop has the same maximum frequency

    # Print the result
    if count > 1:
        print("CONFUSED")
    else:
        print(max_laptop)
