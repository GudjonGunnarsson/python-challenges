#!/usr/bin/python3
""" This challenge is as follows:
    We have a loud talking parrot. The "hour"
    parameter is the current hour time in the range
    0..23. We are in trouble if the parrot is talking
    and the hour is before 7 or after 20. Return
    True if we are in trouble.

    Expected Results:
        True, 6 -> True
        True, 7 -> False
        False, 6 -> False """

def parrot_trouble(talking, hour):
    # This part is where the challenge is supposed to be solved
    return True if talking and (hour < 7 or hour > 20) else False


if __name__ == '__main__':
    # This part is only to test if challenge is a success
    print("Scenario 1: True, 6: {}".format("success" if parrot_trouble(True, 6) else "fail"))
    print("Scenario 2: True, 7: {}".format("success" if not parrot_trouble(True, 7)  else "fail"))
    print("Scenario 3: False, 6: {}".format("success" if not parrot_trouble(False, 6) else "fail"))
    print("Scenario 4: True, 21: {}".format("success" if parrot_trouble(True, 21) else "fail"))
