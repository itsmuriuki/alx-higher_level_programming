#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return str
    str1 = str[0:n] + str[n + 1:]
    return str1
