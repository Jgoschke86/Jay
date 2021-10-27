#!/usr/bin/python3

from zipfile import ZipFile,ZIP_DEFLATED
import os.path

# reading & extracting
rzip = ZipFile("../DATA/textfiles.zip")
print(rzip.namelist())
ty = rzip.read('tyger.txt')
print(ty[:50])
rzip.extract('parrot.txt')

# creating a zip file
wzip = ZipFile("example.zip",mode="w",compression=ZIP_DEFLATED)
for base in "parrot tyger knights alice poe_sonnet spam".split():
    filename = os.path.join("../DATA",base + '.txt')
    print("adding {0} as {1}".format(filename,base + '.txt')) 
    wzip.write(filename,base + '.txt')
