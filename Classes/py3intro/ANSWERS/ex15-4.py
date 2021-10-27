#!/usr/bin/python3

from president import President

for i in range(1,45):
    p = President(i)
    print(p.FirstName, p.LastName,p.BirthDay, p.DeathDay, p.Party)