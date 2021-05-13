#!/usr/bin/env python3
asterisk = "*"

for num in range(9):
    print(asterisk)
    if num < 4:
        asterisk += " *"
    else:
        asterisk = asterisk[:-2]
