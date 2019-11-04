m = [[0,0,0],[1,1,1],[2,2,2],[3,3,3],[4,4,4],[5,5,5],[6,6,6]]
score = []
q = 1
for i in range(0,6):
    w = m[q]
    e = w[2]
    score.append(e)
    q += 1
print(score)