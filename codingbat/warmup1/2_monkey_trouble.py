#!/usr/bin/python3
""" This challenge is as follows:
    We have two monkeys, a and b, and the parameters
    a_smile and b_smile indicate if each is smiling.
    We are in trouble if they are both smiling or if
    neither of them is smiling. Return True if we are
    in trouble.

    Expected Results:
        False, False -> True
        True, False  -> False
        False, True  -> False
        True, True   -> True """


def monkey_trouble(a_smile, b_smile):
    # This part is where the challenge is supposed to be solved
    return True if (a_smile and b_smile) or (not a_smile and not b_smile) else False
    


if __name__ == '__main__':
    # This part is only to test if challenge is a success
    print("Scenario 1: False, False: {}".format("success" if monkey_trouble(False, False) else "fail"))
    print("Scenario 2: True, False: {}".format("success" if not monkey_trouble(True, False) else "fail"))
    print("Scenario 3: False, True: {}".format("success" if not monkey_trouble(False, True) else "fail"))
    print("Scenario 4: True, True: {}".format("success" if monkey_trouble(True, True) else "fail"))
