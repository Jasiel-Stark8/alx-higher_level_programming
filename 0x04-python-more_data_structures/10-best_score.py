#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:  # Return None if dict is empty
        return None
    return max(a_dictionary, key=a_dictionary.get())
# print(best_score({1: 2, 2: 4, 3: 6}))
