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


# Your code goes here
while token != "q":
    expression = raw_input()
    tokens_list = expression.split(" ")
    if tokens_list[0] == "q":
        token = "q"

    elif tokens_list[0] == "+":
        add(tokens_list[1], tokens_list[2])
        

