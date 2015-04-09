# Your code goes here
"""
calculator.py
Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
if tokens[0] is equal to "pow":
    call the power function with the other two tokens
# No setup
repeat forever:
    read input
    tokenize input
    if the first token is 'q', quit
    otherwise decide which math function to call based on the tokens we read
"""

from arithmetic import *
OPERATOR = 0
NUM1 = 1
NUM2 = 2

# Your code goes here
while True:
    expression = raw_input()
    tokens_list = expression.split(" ")

    if tokens_list[OPERATOR] == "q":
        break

    if tokens_list[OPERATOR] == "+":
        print add(tokens_list[NUM1], tokens_list[NUM2])

    elif tokens_list[OPERATOR] == "-":
        print subtract(tokens_list[NUM1], tokens_list[NUM2])

    elif tokens_list[OPERATOR] == "*":
        print multiply(tokens_list[NUM1], tokens_list[NUM2])

    elif tokens_list[OPERATOR] == "/":
        print divide(tokens_list[NUM1], tokens_list[NUM2])

    elif tokens_list[OPERATOR] == "square":
        print square(tokens_list[NUM1])

    elif tokens_list[OPERATOR] == "cube":
        print cube(tokens_list[NUM1])

    elif tokens_list[OPERATOR] == "pow":
        print power(tokens_list[NUM1], tokens_list[NUM2])

    elif tokens_list[OPERATOR] == "mod":
        print mod(tokens_list[NUM1], tokens_list[NUM2])
