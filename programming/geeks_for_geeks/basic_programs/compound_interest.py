# Python Program for Compound Interest

def get_compound_interest(principle_amount,rate,time):
    result = principle_amount * (pow((1 + rate/100), time)) 
    compound_interest = result - principle_amount
    print(compound_interest)
    return compound_interest

principle_amount = float(input("enter amount: \n"))
rate = float(input("rate: \n"))
time = float(input("time: \n"))
get_compound_interest(principle_amount,rate,time)
    