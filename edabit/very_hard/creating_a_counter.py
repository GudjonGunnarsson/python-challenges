#!/usr/bin/python3
""" Reference: https://edabit.com/challenge/oo5zkiydtRB344ZcL
    This challenge is as follows:
    Create a function that returns how many times it's been
    called previously.
    Do not use a global variable.

    Expected Results:
        counter() -> 0
        counter() -> 1
        counter() -> 2 """

def counter():
    # This part is where the challenge is supposed to be solved
    counter.c += 1
    return counter.c

counter.c = -1

if __name__ == '__main__':
    # This part is only to test if challenge is a success
    print("Scenario 1: {}".format("success" if counter() == 0 else "fail"))
    print("Scenario 2: {}".format("success" if counter() == 1 else "fail"))
    print("Scenario 3: {}".format("success" if counter() == 2 else "fail"))
