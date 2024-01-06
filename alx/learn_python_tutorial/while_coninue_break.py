#!/usr/bin/python3

import random

i = 0

while (i < 20):
    if ((i % 2) == 0):
        i += 1
        continue
    if (i == 15):
        break
    print(f'{i} is an odd number')
    i += 1
