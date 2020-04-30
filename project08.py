"""
Course: CS101
File: Project 08 
Project: 08
Author: Alfredo Pena 

Description:
  It tells the user their tax rate according to income and status. 
"""

"""
Instructions:

Complete the two functions below so they calculate the correct tax rates.

"""

import random

# TODO - Complete this function

def calculateSingleTax(monthlyIncome):
    """calculateSingleTax - given monthly income, it returns the tax rate"""
    a = monthlyIncome * 12
    if a == 0:
        return 0 
    elif  1 <= a <= 9525:
        return 10
    elif 9526 <= a <=  38700:
        return 12
    elif 38701 <= a <= 82500:
        return 22
    elif 82501 <= a <=  157500:
        return 24
    elif 157501 <= a <= 200000:
        return 32
    elif 200001 <= a <= 500000:
        return 35
    else:
        return 37
    

# TODO - Complete this function

def calculateMarriedTax(husbandIncome, wifeIncome):
    """calculateMarriedTax - given yearly incomes for both husband
    and wife, return the married tax rate"""
    pass
    a = husbandIncome + wifeIncome
    if a == 0:
        return 0 
    elif  1 <= a <= 19050:
        return 10
    elif 19051 <= a <=  77400:
        return 12
    elif 77401 <= a <= 165000:
        return 22
    elif 165001 <= a <=  315000:
        return 24
    elif 315001 <= a <= 400000:
        return 32
    elif 400001 <= a <= 600000:
        return 35
    else:
        return 37

# =======================================================================
# Main code - Do not change any code below this comment.

"""
Testing calculateSingleTax().  To pass all of these tests, you must
implement the tax rate table and have calculateSingleTax() return the
correct tax rate for these monthly income values.

If one of more of these asserts() fail (ie., stop your program), you
must fix the issue in the calculateSingleTax() function.
"""

assert(calculateSingleTax(0) == 0)
assert(calculateSingleTax(593) == 10)
assert(calculateSingleTax(793) == 10)
assert(calculateSingleTax(794) == 12)

assert(calculateSingleTax(2725) == 12)
assert(calculateSingleTax(6693) == 22)
assert(calculateSingleTax(9797) == 24)
assert(calculateSingleTax(15584) == 32)
assert(calculateSingleTax(37518) == 35)
assert(calculateSingleTax(41666) == 35)
assert(calculateSingleTax(42695) == 37)

print('You passed all of the tests for calculateSingleTax()')


"""
Testing calculateMarriedTax().  To pass all of these tests, you must
implement the tax rate table and have calculateMarriedTax() return the
correct tax rate for these yearly income values for a married couple.

If one of more of these asserts() fail (ie., stop your program), you
must fix the issue in the calculateMarriedTax() function.
"""

assert(calculateMarriedTax(0, 0) == 0)
assert(calculateMarriedTax(0, 1) == 10)
assert(calculateMarriedTax(1, 0) == 10)
assert(calculateMarriedTax(593, 345) == 10)
assert(calculateMarriedTax(6794, 13002)  == 12)

assert(calculateMarriedTax(32725, 12345) == 12)
assert(calculateMarriedTax(36693, 42345) == 22)
assert(calculateMarriedTax(109797, 72345) == 24)
assert(calculateMarriedTax(315584, 42345) == 32)
assert(calculateMarriedTax(337518, 99245) == 35)
assert(calculateMarriedTax(341666, 62345) == 35)
assert(calculateMarriedTax(242695, 472345) == 37)

print('You passed all of the tests for calculateMarriedTax()')