#!/usr/bin/python3
""" This challenge is as follows:
    Gicen a non-empty string and an int n,
    return a new string where the char at
    index n has been removed. The value of
    n will be a valid index of a char in the
    original string (i.e. n will be in the
    range 0..len(str)-1 inclusive).

    Expected Results:
        'kitten', 1 -> 'ktten'
        'kitten', 0 -> 'itten'
        'kitten', 4 -> 'kittn' """

def missing_char(str, n):
    # This part is where the challenge is supposed to be solved
    return str[:n] + str[n+1:]

if __name__ == '__main__':
    # This part is only to test if challenge is a success
    print("Scenario 1: kitten, 1: {}".format("success" if missing_char('kitten', 1) == 'ktten' else "fail"))
    print("Scenario 2: kitten, 0: {}".format("success" if missing_char('kitten', 0) == 'itten' else "fail"))
    print("Scenario 3: kitten, 4: {}".format("success" if missing_char('kitten', 4) == 'kittn' else "fail"))
