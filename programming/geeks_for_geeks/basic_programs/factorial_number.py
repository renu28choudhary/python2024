# factorial of anumber
#recursive function
num = int(input("enter a number: "))

def get_factorial(n):
    if n == 0 or n==1 :
        return 1
    else:
        return n * get_factorial(n - 1)
print(get_factorial(num))

#inbuilt function

import math
a=5
print(math.factorial(a))