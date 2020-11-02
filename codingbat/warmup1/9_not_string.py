#!/usr/bin/python3
""" This challenge is as follows:
    Given a string, return a new string where
    "not" has been added to the front. However,
    if the string already begins with "not",
    return the string unchanged.

    Expected Results:
        'candy'   -> 'not candy'
        'x'       -> 'not x'
        'not bad' -> 'not bad' """

def not_string(str):
    # This part is where the challenge is supposed to be solved
    return str if str.split()[0] == "not" else "not " + str

if __name__ == '__main__':
    # This part is only to test if challenge is a success
    print("Scenario 1: candy  : {}".format("success" if not_string('candy') == 'not candy' else "fail"))
    print("Scenario 2: x      : {}".format("success" if not_string('x') == 'not x' else "fail"))
    print("Scenario 3: not bad: {}".format("success" if not_string('not bad') == 'not bad' else "fail"))
