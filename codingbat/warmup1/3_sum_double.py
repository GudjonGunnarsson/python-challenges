#!/usr/bin/python3
""" This challenge is as follows:
    Given two int values, return their sum.
    Unless the two values are the same, then return
    double their sum.

    Expected Results:
         1, 2 ->  3
         3, 2 ->  5
         2, 2 ->  8
        -1, 0 -> -1
         3, 3 -> 12
         0, 0 ->  0
         0, 1 ->  1
         3, 4 ->  7"""

def sum_double(a, b):
    # This part is where the challenge is supposed to be solved
    return (a + b)*2 if (a == b) else (a + b)


if __name__ == '__main__':
    # This part is only to test if challenge is a success
    print("Scenario 1:  1, 2: {}".format("success" if sum_double(1, 2) == 3 else "fail"))
    print("Scenario 2:  3, 2: {}".format("success" if sum_double(3, 2) == 5 else "fail"))
    print("Scenario 3:  2, 2: {}".format("success" if sum_double(2, 2) == 8 else "fail"))
    print("Scenario 4: -1, 0: {}".format("success" if sum_double(-1, 0) == -1 else "fail"))
    print("Scenario 5:  3, 3: {}".format("success" if sum_double(3, 3) == 12 else "fail"))
    print("Scenario 6:  0, 0: {}".format("success" if sum_double(0, 0) == 0 else "fail"))
    print("Scenario 7:  0, 1: {}".format("success" if sum_double(0, 1) == 1 else "fail"))
    print("Scenario 8:  3, 4: {}".format("success" if sum_double(3, 4) == 7 else "fail"))
