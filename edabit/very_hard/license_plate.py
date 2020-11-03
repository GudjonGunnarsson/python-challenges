#!/usr/bin/python3
""" This challenge is as follows:
    Travelling through Europe one needs to pay
    attention to how the license plate in the
    given country is displayed. When crossing the
    border you need to park on the shoulder,
    unscrew the plate, re-group the characters
    according to the local regulations, attach it
    back and proceed with the journey.

    Create a solution that can format the dmv
    number into a plate number with correct grouping.
    The function input consists of string s and
    group length n. The output has to be upper case
    characters and digits. The new groups are made
    from right to left and connected by -.
    The original order of the dmv number is preserved.
    Expected Results:
        "5F3Z-2e-9-w", 4 -> "5F3Z-2E9W"
        "2-5g-3-J", 2    -> "2-5G-3J"
        "2-4A0r7-4k", 3  -> "24-A0R-74K"
        "nlj-206-fv", 3  -> "NL-J20-6FV """

def license_plate(s, n):
    # This part is where the challenge is supposed to be solved
    # First, remove all dashes and make uppercase
    s = s.replace("-", "").upper()
    # get index of char before first dash (from right)
    char_count = len(s) - 1 - n
    while(char_count >= 0):
        # add a dash after index position char_count
        s = s[:char_count +1] + '-' + s[char_count + 1:]
        # 'increment' counter backwards kind of..
        char_count = char_count - n
    return s


if __name__ == '__main__':
    # This part is only to test if challenge is a success
    print("Scenario 1: 5F3Z-2e-9-w, 4: {}".format("success" if license_plate("5F3Z-2e-9-w", 4) == "5F3Z-2E9W" else "fail"))
    print("Scenario 2: 2-5g-3-J, 2: {}".format("success" if license_plate("2-5g-3-J", 2) == "2-5G-3J" else "fail"))
    print("Scenario 3: 2-4A0r7-4k, 3: {}".format("success" if license_plate("2-4A0r7-4k", 3) == "24-A0R-74K" else "fail"))
    print("Scenario 4: nlj-206-fv, 3: {}".format("success" if license_plate("nlj-206-fv", 3) == "NL-J20-6FV" else "fail"))
