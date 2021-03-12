# IN style_example.py FILE
# What would you say if you were working with someone and this is the code they gave you?

import math
import sys


class Data:
    def __init__(self, df):
        self.df = df

    def null_count(self):
        return self.isnull().sum().sum()

    def list_2_series(self, li):
        return self.append(li)


def example1():
    # This is a long comment and should be wrapped
    # to fit within a 72 character limit
    some_tuple = (1, 2, 3, "a")
    some_variable = {
        "long": "LONG CODE LINES should be wrapped within "
                "79 character to prevent page cutoff stuff",
        "other": [
            math.pi,
            100,
            200,
            300,
            9999292929292,
            "This IS a long string that looks gross and goes beyond what it should",
        ],
        "more": {"inner": "THIS whole logical line should be wrapped"},
        "data": [444, 5555, 222, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 5],
    }
    return some_tuple, some_variable


def example_2():
    return {"has_key() is deprecated": True}


class Example3:
    def __init__(self, bar, some_string):
        self.bar = int(bar)
        self.some_string = some_string

    def eval_bar(self):
        if self.bar:
            self.bar += 1
            self.bar = self.bar * self.bar
            return self.bar
        else:
            return sys.path, self.some_string


pass
