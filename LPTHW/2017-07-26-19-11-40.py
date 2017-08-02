#!/usr/bin/env python
# -*- coding: utf-8 -*-
################################################################################80
## => INFO
################################################################################80
## FILENAME: ex21.py
## DATE: 2017-07-26
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
##   - "笨办法"学Python: [douban link](https://book.douban.com/subject/26264642/)
##
################################################################################80
## => IMPORT MODULES
################################################################################80


################################################################################80
## => 21. Functions Can Return Something
################################################################################80

def add(a,b):
    print "ADDING %d + %d" %(a,b)
    return a+b

def substract(a,b):
    print "SUBSTRCATING %d - %d" %(a,b)
    return a-b

def multiply(a,b):
    print "MULTIPLYING %d * %d" %(a,b)
    return a*b

def divide(a,b):
    print "DIVIDING %d / %d" %(a,b)
    return a/b


print "Let's do some math with just functions!"

age = add(30,5)
id1 = id(age)
age = add(30,5 )
# age = add(30,6)

height = substract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" %(age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle"

what = add(age, substract(height, multiply(weight, divide(iq,2))))
# print id1-id(age)
print "That becomes: ", what, "Can you do it by hand?"

################################################################################80
## => Study Drills
################################################################################80
##
##
##
################################################################################80
## => CHANGELOG
################################################################################80
##
## - 2017-07-26 --create
