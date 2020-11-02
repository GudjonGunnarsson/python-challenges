#!/usr/bin/python3
""" This challenge is as follows:
    The parameter weekday is True if it is a weekday,
    and the parameter vacation is True if we are on 
    vacation. We sleep in if it is not a weekday or
    we're on a vacation. Return True if we sleep in.
    Expected Results:
        False, False -> True
        True, False  -> False
        False, True  -> True
        True, True   -> True """


def sleep_in(weekday, vacation):
    # This part is where the challenge is supposed to be solved
    if weekday:
        return True if vacation else False
    return True


if __name__ == '__main__':
    # This part is only to test if challenge is a success
    print("Scenario 1: False, False: {}".format("success" if sleep_in(False, False) else "fail"))
    print("Scenario 2: True, False: {}".format("success" if not sleep_in(True, False) else "fail"))
    print("Scenario 3: False, True: {}".format("success" if sleep_in(False, True) else "fail"))
    print("Scenario 4: True, True: {}".format("success" if sleep_in(True, True) else "fail"))
