#!/usr/bin/python3
""" This challenge is as follows:
    Given an int n, return the absolute difference
    between n and 21, except return double the
    absolute difference if n is over 21.

    Expected Results:
        19 -> 2
        10 -> 11
        21 -> 0 """

def diff21(n):
    # This part is where the challenge is supposed to be solved
    return (n - 21)*2 if n > 21 else (21 - n)


if __name__ == '__main__':
    # This part is only to test if challenge is a success
    print("Scenario 1: 19: {}".format("success" if diff21(19) == 2 else "fail"))
    print("Scenario 2: 10: {}".format("success" if diff21(10) == 11 else "fail"))
    print("Scenario 3: 21: {}".format("success" if diff21(21) == 0 else "fail"))
    print("Scenario 4: 22: {}".format("success" if diff21(22) == 2 else "fail"))
    print("Scenario 5: -2: {}".format("success" if diff21(-2) == 23 else "fail"))
    print("Scenario 6: 50: {}".format("success" if diff21(50) == 58 else "fail"))
