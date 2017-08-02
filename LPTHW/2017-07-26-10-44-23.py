#!/usr/bin/env python
# -*- coding: utf-8 -*-
################################################################################80
## => INFO
################################################################################80
## FILENAME: ex10.py
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
##   - [Learn Python the Hard Way](https://learnpythonthehardway.org/book)\
##     [douban link](https://book.douban.com/subject/11941213/)
##
################################################################################80
## => IMPORT MODULES
################################################################################80


################################################################################80
## => 10. What Was That?
################################################################################80

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

################################################################################80
## => Escape Sequences
################################################################################80

# while True:
#     for i in ["/","-","|","\\","|"]:
#         print "%s\r" %i,

################################################################################80
## => Study Drills
################################################################################80

## D2
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''
print fat_cat

## D3



## D4

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''
print "Now I'm using %%r format: %r" % fat_cat
print "Now I'm using %%s format: %s" % fat_cat


################################################################################80
## => CHANGELOG
################################################################################80
##
## - 2017-07-26 --create
