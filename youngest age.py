age1=int(input("enter the age"))
age2=int(input("enter the age"))
age3=int(input("enter the age"))
age4=int(input("enter the age"))
if age1<age2 and age1<age3 and age1<age4:
   print(age1,"is yougest person")
if age2<age1 and age2<age3 and age2<age4:   
   print(age2,"is youngest person")
if age3<age1 and age3<age2 and age3<age4:
   print(age3,"is youngest person") 
if age4<age1 and age4<age2 and age4<age3:
   print(age4,"is youngest person")   
else: 
   print("not youngest person")