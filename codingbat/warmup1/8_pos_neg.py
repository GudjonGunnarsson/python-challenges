#!/usr/bin/python3
""" This challenge is as follows:
    Given 2 int values, return True if one is
    negative and one is positive. Except if the
    parameter "negative" is True, then return
    True only if both are negative.

    Expected Results:
         1, -1, False -> True
        -1,  1, False -> True
        -4, -5, True  -> True """

def pos_neg(a, b, negative):
    # This part is where the challenge is supposed to be solved
    return (a < 0 and b < 0) if negative else ((a < 0 and b > 0) or (a > 0 and b < 0))

if __name__ == '__main__':
    # This part is only to test if challenge is a success
    print("Scenario 1:  1, -1, False: {}".format("success" if pos_neg(1, -1, False) else "fail"))
    print("Scenario 2: -1,  1, False: {}".format("success" if pos_neg(-1, 1, False)  else "fail"))
    print("Scenario 3: -4, -5, True: {}".format("success" if pos_neg(-4, -5, True) else "fail"))
