#!/usr/bin/python3

users_by_shell = {}
with open("../DATA/passwd") as passwd_in:
    for line in passwd_in:
        (_, _, _, _, _, _, shell) = line[:-1].split(":")
        if shell == "":
            shell = "NONE"

        if shell in users_by_shell:
            users_by_shell[shell] = users_by_shell[shell] + 1
        else:
            users_by_shell[shell] = 1

for shell, count in users_by_shell.items():
    print("{0:5d} {1}".format(count, shell))
