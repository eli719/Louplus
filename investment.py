#!/usr/bin/env python3
amount = float(input("enter amount: "))
inrate = float(input("enter Interest rate: "))
period = int(input("ENTER period: "))
value = 0
year = 1
while year <= period:
    value  = amount + (inrate * amount)
    print("year {} Rs. {:.2f}".format(year,value))
    amount = value
    year += 1
