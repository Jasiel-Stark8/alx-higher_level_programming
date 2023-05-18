def best_score(a_dictionary):
    if not a_dictionary:  # if the dictionary is empty, return None
        return None
    return max(a_dictionary, key=a_dictionary.get)
