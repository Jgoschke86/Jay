#!/usr/bin/python3

fruit1 = set()
fruit2 = set()

with open("../DATA/fruit1.txt","r") as fruit1_in:
    for f in fruit1_in:
        fruit1.add(f.strip().lower())

with open("../DATA/fruit2.txt","r") as fruit2_in:
    for f in fruit2_in:
        fruit2.add(f.strip().lower())

common_fruits = fruit1 & fruit2

print("\n".join(common_fruits))
