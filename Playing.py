dice = [3,3,4,7,2,1]
p = []
q = 1

for i in range(0,6):
    t = dice.count(q)
    p.append(t)
    q += 1
if 4 in p or 5 in p:
    total = sum(p)
    print(total)
print(p)