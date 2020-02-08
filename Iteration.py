"""Iteration = Loops -> while,for loops"""
import math
def print_n(text,times):
    while times>0: #loop until consdition is false
        print(text)
        times = times-1 #decrementation
    return

#print_n("HELLO",5)

"""Excersise 7-1 Sqaure root estimation"""

def mysquare(a):
    """Computes the square root according to newtons method by giving
    a: the number that one should take the square root on
    x: the initial estimate of the result
    y: the new estimate acc to newtons method"""
    x = a/2
    while True:
        #print(x)
        y = (x + a/x) / 2

        if y == x:
            return y
            break

        x = y


#print(mysquare(100))

def test_square_root():
    a=0
    b=0
    c=0
    d=0

    print("a  mysqrt(a)  math.sqrt(a)  diff")
    print("-  ---------  ------------  ----\n")

    for a in range(9) :
        a=a+1
        b=mysquare(a)
        c=math.sqrt(a)
        d=abs(b-c)
        print (a,"  ",b,"  ",c,"  ",d,)

#test_square_root()

"Excersise 7-2 ------------EVAL-----------------------------"

def eval_loop():
    while True:
        x=input("Please enter something\n")

        if eval(x)=="done":
            return eval(x)

        print(eval(x))


#eval_loop()

"Excersise 7-3------------Numerical-approximation-of-pi------------"

def estimate_pi():
    term=0
    k=0
    total=0
    factor= (2*math.sqrt(2)/(9801))
    while True:
        numerator =     ( math.factorial(4*k) * (1103 + 26390*k) )
        denominator =   ((math.factorial(k)**4)*(396**(4*k)))
        term =          numerator/denominator
        total= total + factor*(term)
        if abs(term)<1e-15:
            break
        k=k+1

    return 1/total

print(estimate_pi())
