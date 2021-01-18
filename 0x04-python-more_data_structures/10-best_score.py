#!/usr/bin/python3
def best_score(a_dictionary):
    score = 0
    res =""
    if a_dictionary:
        for k, v in a_dictionary.items():
            if v > score:
                res = k
                score = v
        return res
    else:
        return None
