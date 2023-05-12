#!/usr/bin/python3
def remove_char_at(str, n):
    for i in str:
        if i == str[n]:
            return str[:n] + str[n + 1:]
        else:
            return str
print(remove_char_at('chicago', 15))
