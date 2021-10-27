
import sys
from dvd import DVD
from cd import CD

# testing...
d1 = DVD('Rear Window')
print(d1.Title)

c1 = CD('Abbey Road')
print(c1.Title)
c1.AddTrack('Something',5,23)
c1.AddTrack('Come Together',7,8)

for t in c1.Tracks:
    print('\t{0.Name:20s} {0.Length}'.format(t))
    