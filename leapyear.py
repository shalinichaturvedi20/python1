year=int(input("enter the year"))
if year%100==0:
    if year%400==0:
        print(year,"is leap year")  
    else:
        (year,"is not leap year")
else:
    if year%4==0:
        print(year,"is leap year") 
    else:
        print(year,"is not leap year")                         