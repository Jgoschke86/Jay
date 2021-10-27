#!/bin/bash

rm -f tauntmodule.o taunt.so taunt.so.1.0

gcc -c -I/usr/include/python2.7 tauntmodule.c
gcc -shared -Wl,-soname,taunt.so.1.0 -o taunt.so.1.0 tauntmodule.o
ln -f -s taunt.so.1.0 taunt.so
