# We need to find simple interest on Rs. 10,000 at the rate of 5% for 5 units of time.

def get_interest(amount,rate,time):
    result = (amount * rate * time) / 100
    print("simple interest",result)
    return result
get_interest(10000,5,5)