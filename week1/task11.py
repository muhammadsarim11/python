# program to calculate monthly emi for a loan 

p = float(input("Enter amount loan: " ))
annual_rate = float(input("Enter annual rate: " ))
years = int(input("Enter loan duration: " ))


r = (annual_rate /100)/12
n= years*12
EMT = (p*r *(1+r)**n /(1+r)**n-1)

print("Monthly EMT:",round(EMT,2))