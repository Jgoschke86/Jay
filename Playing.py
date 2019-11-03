m = [1,2,3,4,4,4,5]
o = []
p = 1
for i in range(0,6):
    o.append(m.count(p))
    p += 1
print(o)