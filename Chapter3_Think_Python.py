#Excersise 3-1 
def right_justify(s):
    length = len(s)
    print(" " * (70-length) + s)

right_justify("MONTY")

#Excersise 3-2
def do_twice(function,val):
    function(val)
    function(val)
    
def print_twice(bruce):   
    print(bruce)    
    print(bruce) 
    
def print_spam():
    print("5"*10)

do_twice(print_twice,"spam") 

def do_four(function,val):
    do_twice(function,val)
    do_twice(function,val)

do_four(print_twice,"spam")

#Excersise 3-3
#Part 1 

def row_seperation_lines():
    print("+","-","-","-","-",'+',"-","-","-","-","+")

def column_lines():
    print("|"," "," "," "," ","|"," "," "," "," ","|")
    
def do_twice(function):
    function()
    function()

def do_four(function):
    do_twice(function)
    do_twice(function)

def built_grid():
    print("+","-","-","-","-",'+',"-","-","-","-","+")
    do_four(column_lines)
    print("+","-","-","-","-",'+',"-","-","-","-","+")
    do_four(column_lines)
    print("+","-","-","-","-",'+',"-","-","-","-","+")


#built_grid()

#Part2 

def built_rows():
    print("+","-","-","-","-",'+',"-","-","-","-","+", end=" ")
    print("-","-","-","-",'+',"-","-","-","-","+")
def built_columns():
    print("|"," "," "," "," ","|"," "," "," "," ","|", end=" ")
    print( " "," "," "," ","|"," "," "," "," ","|")
    
def built_first_stage():
    built_rows()
    do_four(built_columns)
    
def built_four(): 
    do_four(built_first_stage)
    built_rows()
    
built_four()
    
