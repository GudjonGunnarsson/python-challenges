#!/usr/bin/python3
""" This challenge is as follows:
    Given an int n, return True if it is within
    10 of 100 or 200. Note: abs(num) computes
    the absolute value of a number.

    Expected Results:
        93 -> True
        90 -> True
        89 -> False """

def near_hundred(n):
    # This part is where the challenge is supposed to be solved
    return True if (abs(100 - n) <= 10) or (abs(200 - n) <= 10) else False

if __name__ == '__main__':
    # This part is only to test if challenge is a success
    print("Scenario 1: 93: {}".format("success" if near_hundred(93) else "fail"))
    print("Scenario 2: 90: {}".format("success" if near_hundred(90)  else "fail"))
    print("Scenario 3: 89: {}".format("success" if not near_hundred(89) else "fail"))
    print("Scenario 3: 190: {}".format("success" if near_hundred(190) else "fail"))
    print("Scenario 3: 211: {}".format("success" if not near_hundred(211) else "fail"))
