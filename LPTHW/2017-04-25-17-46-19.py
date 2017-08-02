# -*- coding: utf-8 -*-
# [Learn Python the Hard Way](https://learnpythonthehardway.org/book)
# [douban link](https://book.douban.com/subject/11941213/)
# ex5.py
rate_in2cm = 2.54
rate_lbs2kg = 0.45359237
my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inch
my_height_in_cm = my_height * rate_in2cm
my_weight = 180 # lbs
my_weight_in_kg = my_weight * rate_lbs2kg
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d cm tall." % my_height_in_cm
print "He's %d pounds heavy." % my_weight
print "He's %d kilogram heavy." % my_weight_in_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)

# CHANGELOG
#
# - 2017-04-25 --create
