#!/usr/bin/python3
def best_score(a_dictionary):
    score = 0
    if score not in a_dictionary:
        return None
    for key in a_dictionary:
        if a_dictionary[key] > score:
            score = a_dictionary[key]
    return score
