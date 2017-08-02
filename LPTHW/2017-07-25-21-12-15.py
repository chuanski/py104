#!/usr/bin/python
# -*- coding: utf-8 -*-
################################################################################80
## => INFO
################################################################################80
## FILENAME: ex7.py
## DATE: 2017-07-25
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
## => 7. More Printing
################################################################################80

print "Mary had a little lamb."
## to output a sentence
print "Its fleece was white as %s" %'snow'
## to output a sentence in replacement the format %s inside the double quotations
## for the string after percentage mark.
print "And everywhere that Mary went."
print "."*10 # what'd that do?
## To print character dot 10 times.

end1 = "C"
## to define a object named 'end1' pointing to a character 'C'
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happens
## removing the comma will result in output the two words "cheese" and "burge" in different lines.
print end1 + end2 + end3 + end4 + end5 + end6,
## to concatenate objects from end1 to end6 together into a string,
## the comma means this line doesn't end.
print end7 + end8 + end9 + end10 + end11 + end12



################################################################################80
## => CHANGELOG
################################################################################80
##
## - 2017-07-25 --create
