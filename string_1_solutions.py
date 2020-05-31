# -----------------Hello Name-----------------

# Given a string name, return a greeting of the form "Hello (name)!".

# -------Solution------
def hello_name(name):
    return "Hello {}!".format(name)


# ---------Make_abba-------

# #Given two strings, a and b, return the result of putting them in the order
# #abba


def make_abba(a, b):
    return a + b + b + a


# -----------Make_tags--------

# Given tag and word strings, create the HTML string with tags around the word


def make_tags(tag, word):
    return "<{}>{}</{}>".format(tag, word, tag)
