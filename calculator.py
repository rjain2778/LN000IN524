princ=float(input("Principal amount"))
year=int(input("Enter the number of year"))
days=int(input("Enter the number of days"))
rate=float(input("Enter the rate"))
increase=0.5*(year*2.0)
rate=rate+increase
amount=0.0
def fd(days,year,rate,princ):
    if days <180:
        amount=princ*pow((1+(rate/100)),year+days/365)
    if days >180:
        amount=princ*pow((1+(rate/100)),year+days/365)
    return amount

p=float(input("Enter investment per month"))
years=int(input("Enter the number of years"))
cr=6.0
increment=0.5*(years*2.0)
cr+=increment
def sip(p,cr,years):
    

if __name__ == "__main__":
    finala=fd(days,year,rate,princ)
    print(finala)