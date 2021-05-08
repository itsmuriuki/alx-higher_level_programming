#!/usr/bin/python3
for letter in range(122, 96, -1):
    if letter % 2 == 1:
        letter = letter - 32
    print("{:c}".format(letter), end='')
