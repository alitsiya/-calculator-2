"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
while True:
    "input arithmetic problem"
    #intify raw input
    user_input = raw_input("")
    user_input = user_input.split(" ")
    #+ str sfsfd
    try:
        if len(user_input) > 1:
            user_input[1] = int(user_input[1])
            if len(user_input)==3:
                user_input[2] = int(user_input[2])
       
    except ValueError:
        print "Oops! If you are male, may you become eligible to apply to Hackbright!"  
        break
    if user_input[0] =="+":
        print add(user_input[1],user_input[2])
    elif user_input[0] =="-":
        print subtract(user_input[1],user_input[2])
    elif user_input[0] == "*":
        print multiply(user_input[1], user_input[2])
    elif user_input[0] == "/":
        print divide(user_input[1], user_input[2])
    elif user_input[0] == "square":
        print square(user_input[1])
    elif user_input[0] == "cube":
        print cube(user_input[1])     
    elif user_input[0] == "pow":
        print power(user_input[1], user_input[2])
    elif user_input[0] == "mod":
        print mod(user_input[1], user_input[2])
    elif user_input[0] =="q"   :
        print "Bye!"
        break 
    else: 
        print "broken"
        break
