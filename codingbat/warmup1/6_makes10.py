#!/usr/bin/python3
""" This challenge is as follows:
    Given 2 ints, a and b, return True if one
    of them is 10 or if their sum is 10.

    Expected Results:
        9, 10 -> True
        9,  9 -> False
        1,  9 -> True """

def makes10(a, b):
    # This part is where the challenge is supposed to be solved
    return True if (a == 10 or b == 10) or (a+b == 10) else False


if __name__ == '__main__':
    # This part is only to test if challenge is a success
    print("Scenario 1: 9, 10: {}".format("success" if makes10(9, 10) else "fail"))
    print("Scenario 2: 9, 9: {}".format("success" if not makes10(9, 9)  else "fail"))
    print("Scenario 3: 1, 9: {}".format("success" if makes10(1, 9) else "fail"))
