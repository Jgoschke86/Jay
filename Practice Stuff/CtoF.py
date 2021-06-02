# close = ["close", "exit", "quit", "q"]

# while True:
#     cel = input("What is the temp in Celsius? ")
#     if cel.lower() in close:
#         break
#     elif cel.isdigit():
#         f = 9 * int(cel) / 5 + 32
#         print("The temperature in Fahrenheit is ", f)
#     else:
#         print("Please enter a valid number.")

# import sys

# while True:
#     if len(sys.argv) == 1:
#         c = input("what is the degree ")
#         if c.lower() in ("q", "quit"):
#             print("Goodbye")
#             break
#         elif c.isdigit():
#             f = 9 * int(c) / 5 + 32
#             print(" the temp is", f)

#     else:
#         c = sys.argv[1]
#         f = 9 * int(c) / 5 + 32
#         print(" the temp is", f)
#         False

    

import sys

while True:
    if len(sys.argv) == 1:
        c = input("what is the degree ")
    else:
        c = sys.argv[1]
    if c.lower() in ("q", "quit"):
        print("Goodbye")
        break
    else:
        f = 9 * int(c) / 5 + 32
        print(" the temp is", f)
        if len(sys.argv) != 1:
            break
    
