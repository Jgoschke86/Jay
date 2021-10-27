#!/bin/bash

rm -f johnmodule.o libjohn.so.1 libjohn.so john.so

gcc -c -I/usr/include/python2.7 johnmodule.c 
gcc -shared -Wl,-soname,john.so.1.0 -o john.so.1.0 johnmodule.o 
ln -f -s john.so.1.0 john.so 

