#!//usr/bin/Python3Lexer

import sys
import os

if len(sys.argv) != 4:
    print("syntax: keepnewest.py DIR EXTENSION NUM-TO-KEEP")
    sys.exit(1)
    
(start_dir,extension, num_to_keep) = sys.argv[1:]
num_to_keep = int(num_to_keep)

files = [ os.path.join(start_dir,f) for f in os.listdir(start_dir) if f.endswith('.' + extension) ]

files = [ (f,os.path.getmtime(f)) for f in files ]

files.sort(key=lambda e: (e[1],e[0]),reverse=True)

for file in files[num_to_keep:]:
    os.unlink(file[0])
