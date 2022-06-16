import math
class sdm:    
    def calc(a,b,o):
        if o=='+':
           print("Addition : ", (a+b))
        elif o=='-':
            print("Subtraction : ", (a-b))
        elif o=='*':
            print("Multiplication : ", (a*b))
        elif o=='/':
            print("Division : ", (a/b))
        elif o=='%':
            print("Reminder : ", (a%b))
        elif o=='^':
            print("Power : ", pow(a,b))
        elif o=='s':
            print("Power : ", math.sqrt(a))
        elif o=='>':
            if a>b:
                print("a is big")
            else:
                print("b is big")        

