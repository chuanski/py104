#!/usr/bin/env python
# -*- coding: utf-8 -*-
################################################################################80
## => INFO
################################################################################80
## FILENAME: ex19.py
##
##   DESCRIPTION:
##
##   INPUTS:
##
##   OUTPUTS:
##
##   NOTE:
##
##   REFERENCES:
##   - Learn Python the Hard Way:[Website](https://learnpythonthehardway.org/book)\
##     [douban link](https://book.douban.com/subject/11941213/)
##
##
##
################################################################################80
## => IMPORT MODULES
################################################################################80
import numpy as np
from numpy import *

################################################################################80
## => Ex19: Functions And Variables
################################################################################80
## define a function with two arguments,
## notice that the declaration end by a colon mark
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    ## enter the body of function cheese_and_crackers
    ## print an integer-type variable cheese_count
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


print "We can just give the function numbers directly:"
## call function cheese_and_crackers with arguments being integer object
cheese_and_crackers(20,30)


print "OR, we can use variables from our scripts:"
amount_of_cheese = 10
amount_of_crackers = 50

## call function cheese_and_crackers with arguments being integer variables
cheese_and_crackers(amount_of_cheese,amount_of_crackers)


print "We can even do math inside too:"
## call function cheese_and_crackers with arguments being mathematical expressions
cheese_and_crackers(10+20,5+6)


print "And we can combine the two, variables and math:"
## call function cheese_and_crackers with arguments being mathematical expressions
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000)
################################################################################80
## => Study Drills
################################################################################80
## D3
def fib(n,m):
    print "The terms of fibonacci series from the %dth to the %dth are:" % (n,m)
    f = range(m)
    f[0] = 1
    f[1] = 1
    for i in range(2,m):
        f[i] = f[i-1]+f[i-2]
    print f[n-1:m]
    return f[n-1:m]



fib(2,10)
fib(2,2+10)

m = 2
n = 4
p = 6

fib(1,m+6)
fib(1,m+n)
fib(m,n)

# print fib(6,10)
print fib(2,5).extend(fib(6,10))

l1 = fib(2,5)
l2 = fib(6,10)
print l1
# print type(l1)
print l2
l1.extend(l2)
print l1
#
# a = range(2)
# b = range(4)
# a.extend(b)
# print a
################################################################################80
## => CHANGELOG
################################################################################80
##
## -  2017-08-01 --create
