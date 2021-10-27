#!/usr/bin/python3

north_america = [ "US", "El Salvador", "Mexico", "Canada" ]
europe = [ "Germany", "France", "Bulgaria", "Estonia", "Wales"]
africa = [ "Benin", "Kenya", "Egypt", "Morocco"]

world = [ north_america, europe, africa ]

print("world[1]", world[1])
print("world[1][2]", world[1][2])

months = [
   (None, 0),
   ("January", 31),
   ("February", 28),
   ("March", 31),
   ("April", 30),
   ("May", 31),
   ("June", 30),
   ("July", 31),
   ("August", 31),
   ("September", 30),
   ("October", 31),
   ("November", 30),
   ("December", 31)
]

fmt = "{0:9s} {1:2d}"
print(fmt.format(months[1][0], months[1][1]))
print(fmt.format(months[6][0], months[6][1]))
print()

for month, numdays in months[1:]:
    print(fmt.format(month, numdays))
