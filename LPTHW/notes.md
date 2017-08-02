---
Date: 2017-04-24
Title: LPTHW阅读笔记
Published: false
Type: post
Tag:
  - Learn Python the Hard Way
  - LPTHW
  - 阅读笔记
Excerpt:
---

- [Learn Python the Hard Way](https://learnpythonthehardway.org/book)，（[douban link](https://book.douban.com/subject/11941213/)）

# 1 A First Good Program

## cS
It seems important to know the names of special characters/symbols, such as #$%^\&, because you need to search for them on the internet using a good search engine when being curious about their functions in a certain programming language.

|Key/Symbol|Explanation|
|---|---|
|~ | Tilde|
|` | Acute, Back quote, grave, grave accent, left quote, open quote, or a push|
|! | Exclamation mark, Exclamation point, or Bang|
|@  | Ampersat, Arobase, Asperand, At, or At symbol|
|\#  | Octothorpe, Number, Pound, sharp, or Hash/Mesh|
|£ | Pounds Sterling or Pound symbol|
|€ | Euro|
|$  | Dollar sign or generic currency|
|¢ | Cent sign|
|¥ | Chinese Yuan|
|§ | Micro or Section|
|%  | Percent|
|° | Degree|
|^  | Caret or Circumflex|
|\&  | Ampersand, Epershand, or And|
|*  | Asterisk and sometimes referred to as star.|
|(  | Open parenthesis|
|)  | Close parenthesis|
|-  | Hyphen, Minus or Dash|
|_  | Underscore|
|+  | Plus|
|=  | Equals, single equal|
|{  | Open Brace, squiggly brackets, or curly bracket|
|}  | Close Brace, squiggly brackets, or curly bracket|
|[  | Open bracket|
|]  | Close bracket|
|&#124;  | Pipe, Or, or Vertical bar|
|\  | Backslash or Reverse Solidus|
|/  | Forward slash, Solidus, Virgule, or Whack|
|:  | Colon|
|;  | Semicolon|
|"  | Quote, Double Quote, Quotation mark, or Inverted commas|
|'  | Apostrophe or Single Quote|
|< | Less Than or Angle brackets|
|> | Greater Than or Angle brackets|
|, | Comma|
|. | Period, dot or Full Stop|
|? | Question Mark|

**SEE MORE**

- [What are the names of the keyboard symbols?](https://www.quora.com/What-are-the-names-of-the-keyboard-symbols)

## Quote and Single Quote

When you want to print something in Python, function 'print' will be used and the text to be showed should be put inside two quotation marks.

- Single quote in two quotation marks
```
print " I'm writing."
```
- Quote in two single quotation marks
```
print 'In the famous Gettysberg Address, President Abraham Lincoln said, "...government of the people, by the people, for the people, shall not perish from the earth."'
```

# 2 Comments And Pound Characters

##  cS

Take your ex2.py file and review each line **going backward**. Start at the last line, and check each word in reverse against what you should have typed.

Why do I have to read code backward?

It's a trick to make your brain not attach meaning to each part of the code, and doing that makes you process each piece exactly. This catches errors and is a handy error-checking technique.

# 3 Numbers And Math
|Symbols|Names|Functions|
|---|---|---|
|\+| plus |addition|
|\-| minus | substraction|
|/ | slash | division|
|\*|asterisk| multiplication|
|% |percent| modulus|
|**|double ..|exponent|
|//|double ..|floor division|
|< |less-than||
|> |greater-than||
|<= |less-than-equal||
|>= |greater-than-equal||
|== | is-equal, double equal ||
|!= | is-not-equal||
|\& | and | binary AND|
|&#124;| pipe char| binary OR |
|\# | octothorpe/pound/hash/mesh|Comments|

# 4 Variables And Names

## Study Drills
```
Traceback (most recent call last):
  File "ex4.py", line 8, in <module>
    average_passengers_per_car = car_pool_capacity / passenger
NameError: name 'car_pool_capacity' is not defined
```
Here that the interpreter mentioned "*** is not defined", means the programmer had called the name of a variable or a function which had not been defined or declared before.
In this certain case, it seems that there is a small typo, 'car_pool_capacity' is supposed to be 'carpool_capacity', so that the interpreter can't know which variable 'car_pool_capacity' is.

# 5 More Variables and Printing

## String Formatting Operator

**SEE MORE**

- [Python Strings](https://www.tutorialspoint.com/python/python_strings.htm)

### String Formatting Operator

Here is the list of complete set of symbols which can be used along with % −

|Format Symbol	|Conversion|
|---|---|
|%c	|character|
|%s	|string conversion via str() prior to formatting|
|%i	|signed decimal integer|
|%d	|signed decimal integer|
|%u	|unsigned decimal integer|
|%o	|octal integer|
|%x	|hexadecimal integer (lowercase letters)|
|%X	|hexadecimal integer (UPPERcase letters)|
|%e	|exponential notation (with lowercase 'e')|
|%E	|exponential notation (with UPPERcase 'E')|
|%f	|floating point real number|
|%F	|Floating point decimal format.|
|%g	|the shorter of %f and %e<br>Same as "e" if exponent is greater than -4 or less than precision, "f" otherwise.|
|%G	|the shorter of %F and %E|
|%r  |String (converts any python object using repr()).|
|%	|No argument is converted, results in a "%" character in the result.

Other supported symbols and functionality are listed in the following table −

|Symbol	|Functionality |
|---|---|
|*	|argument specifies width or precision
|-	|left justification
|+	|display the sign
|<sp>	|leave a blank space before a positive number
|#	|add the octal leading zero ( '0' ) or hexadecimal leading '0x' or '0X', depending on whether 'x' or 'X' were used.
|0	|pad from left with zeros (instead of spaces)
|%	|'%%' leaves you with a single literal '%'
|(var)	|mapping variable (dictionary arguments)
|m.n.	|m is the minimum total width and n is the number of digits to display after the decimal point (if appl.)

# 8: [Printing, Printing](2017-07-25-21-38-00.py)
@2017-07-25
## Study Drills

2. The output string is included inside quotations.
      Usually, they should be single quotations which embrace the string.
      When, occassionally, the string contains a single quotation, the outside
      quotations will become double ones.

# Ex9: [Printing, Printing, Printing](2017-07-25-23-15-33.py)
# Ex10: [What Was That?](2017-07-26-10-44-23.py)
# Ex11: [Asking Questions](2017-08-01-22-21-52.py)
# Ex12: [Prompting People](2017-08-01-23-53-25.py)
# Ex13: [Parameters, Unpacking, Variables](2017-08-01-23-59-09.py)
# Ex14: [Prompting And Passing](2017-08-02-00-10-42.py)
# Ex15: [Reading Files](2017-08-02-00-22-10.py)
# Ex16: [Reading And Writing Files](2017-08-02-14-29-01.py)
# Ex17: [More Files](2017-08-02-14-42-51.py)
# Ex18: [Names, Variables, Code, Functions](2017-08-02-16-31-44.py)
# Ex19: [Functions And Variables](2017-08-01-17-10-34.py)
# Ex20: [Functions And Files](2017-08-01-21-58-00.py)
# Ex21: [Functions Can Return Something](2017-07-26-19-11-40.py)
# Ex22: [What Do You Know So Far?]()
# Ex23: [Read Some Code]()
# Ex24: [More Practice]()
# Ex25: [Even More Practice]()
# Ex26: [Congratulations, Take A Test!]()
# Ex27: [Memorizing Logic]()
# Ex28: [Boolean Practice]()
# Ex29: [What If]()
# Ex30: [Else And If]()
# Ex31: [Making Decisions]()
# Ex32: [Loops And Lists]()
# Ex33: [While Loops]()
# Ex34: [Accessing Elements Of Lists]()
# Ex35: [Branches and Functions]()
# Ex36: [Designing and Debugging]()
# Ex37: [Symbol Review]()
# Ex38: [Doing Things To Lists]()
# Ex39: [Dictionaries, Oh Lovely Dictionaries]()
# Ex40: [Modules, Classes, And Objects]()
# Ex41: [Learning To Speak Object Oriented]()
# Ex42: [Is-A, Has-A, Objects, and Classes]()
# Ex43: [Gothons From Planet Percal #25]()
# Ex44: [Inheritance Vs. Composition]()
# Ex45: [You Make A Game]()
# Ex46: [A Project Skeleton]()
# Ex47: [Automated Testing]()
# Ex48: [Advanced User Input]()
# Ex49: [Making Sentences]()
# Ex50: [Your First Website]()
# Ex51: [Getting Input From A Browser]()
# Ex52: [The Start Of Your Web Game]()

# READ MORE

# CHANGELOG

- 2017-04-24 --create
