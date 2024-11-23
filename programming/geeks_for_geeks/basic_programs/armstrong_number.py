# Python Program to Check Armstrong Number

def check_armstrong_number(n):
    temp = n
    total =0
    digit = len(str(n))
    
    while(n>0):
        i= n%10
        total += i ** digit
        n= n//10  # double line for float leaving decimal point
    if(temp == total):
        print(temp,"Armstrong number")
        return temp
    else:
        print(temp,"Not a Armstrong number")
        return temp
    
n = int(input("enter a number: \n"))
check_armstrong_number(n)