"""
code_with_lint.py
Example Code with lots of lint!
"""

#import io
#from math import pi
#from time import time
#from datetime import datetime

# https://pylint.pycqa.org/en/latest/user_guide/checkers/features.html

SOME_GLOBAL_VAR = 'GLOBAL VAR NAMES SHOULD BE IN ALL_CAPS_WITH_UNDERSCORES'
def func_append_list(x_list):
    """
    This appends a new item to a list
    """
    x_list.append(len(x_list))

def multiply(x_num, y_num):
    """
    This returns the result of a multiplation of the inputs
    """
    #some_local_var = 'this is actually a local variable...'
    result = x_num* y_num
    if result == 777:
        print("jackpot!")
    return result

def is_sum_lucky(x_num, y_num):
    """This returns a string describing whether or not the sum of input is lucky
    This function first makes sure the inputs are valid and then calculates the
    sum. Then, it will determine a message to return based on whether or not
    that sum should be considered "lucky"
    """
    if x_num is not None and y_num is not None:
        result = x_num + y_num
        if result == 7:
            return 'A lucky number'
        return 'An unlucky number'
    return 'One or more numbers were not specified'

    # if x != None:
    #     if y is not None:
    #         result = x+y
    #         if result == 7:
    #             return 'a lucky number!'
    #         else:
    #             return 'an unlucky number!'

    # return 'just a normal number'

class Someclass:
    """
    A class that uses datetime
    """
    def __init__(self, some_arg,  some_other_arg, verbose = False):
        self.some_other_arg  =  some_other_arg
        self.some_arg        =  some_arg
        self.verbose         =  verbose
        #list_comprehension = [((100/value)*pi) for value in some_arg if value != 0]
        #time = time()
        #date_and_time = datetime.now()

    def __repr__(self):
        return self.some_arg
    def __str__(self):
        return "SomeClass"
    