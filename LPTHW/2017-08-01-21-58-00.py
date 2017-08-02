#!/usr/bin/env python
# -*- coding: utf-8 -*-
################################################################################80
## => INFO
################################################################################80
## FILENAME: ex20.py
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
##
################################################################################80
## => IMPORT MODULES
################################################################################80
from sys import argv


################################################################################80
## => Ex20: Functions And Files
################################################################################80


script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count,f):
    print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line,current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)
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
## -  2017-08-01 --create
