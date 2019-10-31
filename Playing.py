new=5
sel=1
m = [[1],[2],[7]]
print(m)
n=m[1]
n.append(new)
m.pop(sel)
m.insert(sel,n)


print(m)