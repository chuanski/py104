# -*- coding: utf-8 -*-
# [Learn Python the Hard Way](https://learnpythonthehardway.org/book)
# [douban link](https://book.douban.com/subject/11941213/)
# ex6.py Strings and Text

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)
yy = 'Those who know %s and those who %s.' % (binary, do_not)
yysq = "Those who know %s and those who %s."
#yysq_1 = "Those who know %s and those who %s." % (binary)
yydq = 'Those who know %s and those who %s.'

# - seems that there is no difference between ' and " \
#   except which kind of quotation you want to output in the whole sentence.
# - if there are no arguements after the formatting string, the '%s' will be \
#   considered as a string but not a format declaration
# - if the number of arguments does not match that of the formatting strings, \
#   the interpreter will report an error.

print x
print y
print yy
print yysq
print yydq

print "I said: %r." % x
print "I also said: '%s'." % y
print "I also said: '"' I said: %s."' % y
print "I also said: ' I said: '%r'." % y

# single and double quotations are used consecutively.

hilarious = False # the first letter 'F' is uppercase.
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w+e

# CHANGELOG
#
# - 2017-04-26 --create
