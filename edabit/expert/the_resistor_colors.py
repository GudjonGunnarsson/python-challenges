#!/usr/bin/python3
""" Reference: https://edabit.com/challenge/EcAKCvatiTzZx5Wov
    This challenge is as follows:
    A resistor is a common electrical component found
    in every electronic circuit. Usually a resistor has
    a color-based code (as painted bands over it) to
    decipher through a table.

    Color       Digits	Magnitude   Tolerance   T.C.R.
    Black	0	0	     -	        -
    Brown	1	1	    +/-1%	100ppm/k
    Red	        2	2	    +/-2%	50ppm/k
    Orange	3	3	    -	        15ppm/k
    Yellow	4	4	    -	        25ppm/k
    Green	5	5	    +/-0.5%	-
    Blue	6	6	    +/-0.25%	10ppm/k
    Violet	7	7	    +/-0.1%	5ppm/k
    Gray	8	8	    +/-0.05%	-
    White	9	9	    -	        -
    Gold	-	-1	    +/-5%	-
    Silver	-	-2	    +/-10%	-
    Starting from the left assign a number to each coloured band:

    4 bands resistor:
        1st and 2nd color: digits from column 1.
        3rd color: 10 elevated to the digit of column 2.
        4th color: tolerance from column 3.
    5 bands resistor:
        1st, 2nd and 3rd color: digits from column 1.
        4th color: 10 elevated to the digit of column 2.
        5th color: tolerance from column 3.
    6 bands resistor:
        From 1st to 5th: as above.
        6th color: coefficient from column 4.

    Then, when numbers have replaced colors:
        Resistance is equal to the number resulting by the union
        of digits from column 1 multiplied for the magnitude
        calculated from column 2: is measured in Ohms (symbol: Ω).
        When Ohms are in the thousands order the notation is
        kΩ (kiloOhms), in the millions order the notation is
        MΩ (MegaOhms), in the billions order the notation is
        GΩ (GigaOhms).
        Tolerance and TCR (temperature coefficient of resistance,
        only for 6-banded resistors) are the results of columns 3 and 4.

    Given a list of colors you must return the resistor resistance,
    tolerance and (eventually) the TCR as a string (with identifiers
    separated by spaces between them).

    Note: All given lists are valid, no exceptions to handle. """

def get_unit(val):
    # this feels ghetto
    if val >= 1000000000:
        val = str(val)
        return "{}G".format(val[:-9])
    elif val >= 1000000:
        val = str(val)
        return "{}M".format(val[:-6])
    elif val >= 1000:
        val = str(val)
        return "{}k".format(val[:-3])
    else:
        return "yo wrong numba"

def resistor_code(list_of_codes):
    # This part is where the challenge is supposed to be solved
    plus_minus = "+/-"
    ppm = "ppm/k"
    tab = {
            "black": {"digits": 0, "magnitude": 0, "tolerance": None, "tcr": None},
            "brown": {"digits": 1, "magnitude": 1, "tolerance": 1, "tcr": 100},
            "red": {"digits": 2, "magnitude": 2, "tolerance": 2, "tcr": 50},
            "orange": {"digits": 3, "magnitude": 3, "tolerance": None, "tcr": 15},
            "yellow": {"digits": 4, "magnitude": 4, "tolerance": None, "tcr": 25},
            "green": {"digits": 5, "magnitude": 5, "tolerance": 0.5, "tcr": None},
            "blue": {"digits": 6, "magnitude": 6, "tolerance": 0.25, "tcr": 10},
            "violet": {"digits": 7, "magnitude": 7, "tolerance": 0.1, "tcr": 5},
            "gray": {"digits": 8, "magnitude": 8, "tolerance": 0.05, "tcr": None},
            "white": {"digits": 9, "magnitude": 9, "tolerance": None, "tcr": None},
            "gold": {"digits": None, "magnitude": -1, "tolerance": 5, "tcr": None},
            "silver": {"digits": None, "magnitude": -2, "tolerance": 10, "tcr": None}
            }
    if len(list_of_codes) == 4:
        list_of_codes[0] = tab[list_of_codes[0]]["digits"]
        list_of_codes[1] = tab[list_of_codes[1]]["digits"]
        list_of_codes[2] = 10**tab[list_of_codes[2]]["magnitude"]
        list_of_codes[3] = tab[list_of_codes[3]]["tolerance"]

        resistance = int(
                str(list_of_codes[0])
                + str(list_of_codes[1])) * list_of_codes[2]

        res_str = "{}Ohm +/-{}%".format(get_unit(resistance), list_of_codes[3])

        return res_str
    elif len(list_of_codes) == 5:
        list_of_codes[0] = tab[list_of_codes[0]]["digits"]
        list_of_codes[1] = tab[list_of_codes[1]]["digits"]
        list_of_codes[2] = tab[list_of_codes[2]]["digits"]
        list_of_codes[3] = 10**tab[list_of_codes[3]]["magnitude"]
        list_of_codes[4] = tab[list_of_codes[4]]["tolerance"]

        resistance = int(
                str(list_of_codes[0])
                + str(list_of_codes[1])
                + str(list_of_codes[2])) * list_of_codes[3]

        res_str = "{}Ohm +/-{}%".format(get_unit(resistance), list_of_codes[4])

        return res_str
    elif len(list_of_codes) == 6:
        list_of_codes[0] = tab[list_of_codes[0]]["digits"]
        list_of_codes[1] = tab[list_of_codes[1]]["digits"]
        list_of_codes[2] = tab[list_of_codes[2]]["digits"]
        list_of_codes[3] = 10**tab[list_of_codes[3]]["magnitude"]
        list_of_codes[4] = tab[list_of_codes[4]]["tolerance"]
        list_of_codes[5] = tab[list_of_codes[5]]["tcr"]

        resistance = int(
                str(list_of_codes[0])
                + str(list_of_codes[1])
                + str(list_of_codes[2])) * list_of_codes[3]

        res_str = "{}Ohm +/-{}% {}ppm/k".format(
                get_unit(resistance),
                list_of_codes[4],
                list_of_codes[5])

        return res_str

if __name__ == '__main__':
    # This part is only to test if challenge is a success
    print('Scenario 1: ["red", "yellow", "blue", "green"] : {}'.format(
        "success" if resistor_code(["red", "yellow", "blue", "green"]) == "24MOhm +/-0.5%" else "fail"))
    print('Scenario 2: ["white", "black", "white", "blue", "gold"] : {}'.format(
        "success" if resistor_code(["white", "black", "white", "blue", "gold"]) == "909MOhm +/-5%" else "fail"))
    print('Scenario 3: ["black", "white", "black", "orange", "red", "yellow"] : {}'.format(
        "success" if resistor_code(["black", "white", "black", "orange", "red", "yellow"]) == "90kOhm +/-2% 25ppm/k" else "fail"))
