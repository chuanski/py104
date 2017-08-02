#!/usr/bin/env python
# -*- coding: utf-8 -*-
################################################################################80
## => INFO
################################################################################80
## FILENAME: ex15.py
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
from sys import argv


################################################################################80
## => Ex15: Reading Files
################################################################################80


script, filename = argv

txt = open(filename)

print "Here's your file %r." % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()

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
