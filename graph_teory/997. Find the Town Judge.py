n = 3
trust = [[1,3],[2,3]]

trust_score = [0] * (n + 1)

for i, j in trust:
    trust_score[i] = -1
    trust_score[j] += 1

for i in range(len(trust_score)):
    if trust_score[i] == n - 1:
        print(i)