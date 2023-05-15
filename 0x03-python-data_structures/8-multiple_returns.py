#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return len(sentence), None
    for i in sentence:
        if isinstance(i, str):
            return len(sentence), i
    # return len(sentence), None
