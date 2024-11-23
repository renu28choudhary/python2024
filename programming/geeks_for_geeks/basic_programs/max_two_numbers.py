# Maximum of two numbers in Python means largest num
num_1 = 5
num_2 = 6

if(num_1 > num_2) :
    print(num_1, "is largest")
else :
    print(num_2, "is largest")
    
#using function:
n1 = input("n1 \n")
n2 = input ("n2 \n")
def get_largest_number(n1,n2):    
    if n1>=n2: return n1
    else: return n2
print(get_largest_number(n1, n2))