"""
cd into directory where warmup_1.py is kept and run python3 warmup_1.py
"""


def check_sleep_in(weekday: bool, vacation: bool):
    """
    The parameter weekday is True if it is a weekday, and the parameter vacation is
    True if we are on vacation. We sleep in if it is not a weekday or we're on
    vacation. Return True if we sleep in.
    """
    if not weekday or vacation:
        return True
    else:
        return False


def check_monkey_trouble(a_smile: bool, b_smile: bool):
    """
    We have two monkeys, a and b, and the parameters a_smile and b_smile indicate
    if each is smiling. We are in trouble if they are both smiling or if neither of
    is smiling. Return True if we are in trouble.
    """
    if a_smile and b_smile:
        return True
    elif not a_smile and not b_smile:
        return True
    else:
        return False


def sum_double(a: int, b: int):
    """
    Given two int values, return their sum. Unless the two valuse are the same,
    then return double their sum.
    """
    if a == b:
        return (a + b) * 2
    else:
        return a + b


def diff21(n: int):
    """
    Given and int n, return the absolute difference between n and 21, except Return
    double the absolute difference if n is over 21.
    """
    if n > 21:
        return abs(n - 21) * 2
    if n <= 21:
        return abs(21 - n)


def check_parrot_trouble(talking: bool, hour: int):
    """
    We have a loud talking parrot. The "hour" parameter is current hour time in the
    range 0-23. We are in trouble if the parrot is talking and the hour before 7
    or after 20. Return True if we are in trouble.
    """
    quiet_hours: bool = hour > 20 or hour < 7
    if quiet_hours and talking:
        trouble: bool = True
    else:
        trouble: bool = False
    return trouble


def check_makes_ten(a: int, b: int):
    """
    Given 2 ints, a and b, return True if one of them is 10 or if their sum is 10
    """
    sums_to_ten: bool = a + b == 10
    one_is_ten: bool = a == 10 or b == 10
    if sums_to_ten or one_is_ten:
        return True
    else:
        return False


def check_near_hundred(n: int):
    """
    Given and in n, return True if it is within 10 of 100 or 10 of 200.
    """
    if (abs(100 - n) <= 10) or (abs(200 - n) <= 10):
        return True
    else:
        return False


def pos_neg(a: int, b: int, negative: bool = False):
    """
    Given 2 int values, return True if one is negative and one is positive. Except
    if the parameter "negative" is True, then return True only if both are negative.
    """
    if negative:
        return (a < 0 and b < 0)
    else:
        return ((a < 0 and b > 0) or (a > 0 and b < 0))


def add_not(string: str):
    """
    Given a string, return a new string where "not" has been added to the front
    However, if the string already begins with "not", return the string unchanged.
    """
    if string[:3] == 'not':
        return string
    else:
        return "not " + string


if __name__ == "__main__":
    num = 99
    near_hundred = check_near_hundred(num)
    print(f"{num} near 100? {str(near_hundred)}")
