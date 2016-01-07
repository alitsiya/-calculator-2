"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

user_file = open("amy.txt", "r")
output_file = open("output.txt", "w")

# Your code goes here
while True:
    "input arithmetic problem"
    #intify raw input
    # user_input = raw_input("")
    user_input = user_file.readline()
    user_input = user_input.rstrip()
    user_input = user_input.rsplit(" ")
    print user_input
    try:
        if len(user_input) > 1:
            user_input[1] = float(user_input[1])
            if len(user_input)>=3:
                user_input[2] = float(user_input[2])

    except ValueError:
        print "Oops! If you are male, may you become eligible to apply to Hackbright!"  
        break

    # lisofnum = user_input[1:]
    # print reduce((lambda x, y: int(x)+int(y)), lisofnum)

    x=len(user_input)
    numofnums=x-1


    if user_input[0] =="+" and x>2:
        subtotal=add(user_input[1],user_input[2])
        for i in range(3,numofnums+1):
            subtotal=add(subtotal,float(user_input[i]))
        print "{0:.2f}".format(subtotal)   
        output_file.write("{0:.2f}".format(subtotal)) 
    elif user_input[0] =="-":
        print subtract(user_input[1],user_input[2])
    elif user_input[0] == "*":
        print multiply(user_input[1], user_input[2])
    elif user_input[0] == "/":
        print divide(user_input[1], user_input[2])
    elif user_input[0] == "exp":
        print (user_input[1]**user_input[2])    
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
