def solve():
    n = int(input())
    scores = {}
    for _ in range(n):
        p, s = map(int, input().split())
        if 1 <= p <= 8:
            scores[p] = max(scores.get(p, 0), s)

    total_score = sum(scores.get(i, 0) for i in range(1, 9))
    print(total_score)

t = int(input())
for _ in range(t):
    solve()
