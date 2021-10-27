#!/usr/bin/env python

    import os

    os.system("who")
    print()

    with os.popen("ls -l ../DATA","r") as ls:
        for entry in ls:
            print(entry[:-1])
        print()

    # backticks equivalent
    host_name = os.popen("uname -n").read()

    print(host_name)
