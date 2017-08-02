#!/usr/bin/env python
# -*- coding: utf-8 -*-
################################################################################80
## => INFO
################################################################################80
## FILENAME: ex11.py
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
##   - 笨办法学Python: [douban link](https://book.douban.com/subject/26264642/)
##
##
################################################################################80
## => IMPORT MODULES
################################################################################80



################################################################################80
## => Ex11: Asking Questions
################################################################################80
## the comma mark at the end of print line indicates that print doesn't end
## the line with a new line Character and turn to the next line.
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." %(age, height, weight)


################################################################################80
## => Study Drills
################################################################################80
## D1
## A: we use raw_input to receive a string from standard input.
##    see [link](https://docs.python.org/2/library/functions.html#raw_input)
## D2
print "Where do you come from?",
nat = raw_input("==>")

print "Oh, 'seems that you come from %r" % nat
## D4 
################################################################################80
## => CHANGELOG
################################################################################80
##
## -  2017-08-01 --create
