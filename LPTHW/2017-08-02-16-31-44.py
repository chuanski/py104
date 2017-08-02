#!/usr/bin/env python
# -*- coding: utf-8 -*-
################################################################################80
## => INFO
################################################################################80
## FILENAME: ex18.py
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
# this one is like your scripts with argv
def print_two(*args):
    arg1,arg2 = args
    print "arg1:%r, arg2:%r" %(arg1,arg2)

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1:%r, arg2:%r" %(arg1,arg2)

# this just takes one argument
def print_one(arg1):
    print "arg1:%r" %arg1

# this one takes no argument
def print_none():
    print "I got nothin'."


print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
################################################################################80
## => Ex18: Names, Variables, Code, Functions
################################################################################80



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
## -  2017-08-02 --create
