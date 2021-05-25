#num1=int(input("enter the number"))
#num2=int(input("enter the number"))
#num3=int(input("enter the number"))
#if num1>num2 and num1>num3:
    #print(num1,"is maximum number")
#elif num2>num3 and num2>num1:
    #print(num2,"is maximum number")
#else:
   # print(num3,"is maximum number")

num1=int(input("enter the number"))
if num1>0:
    print("positive number")
    num2=int(input("enter the number"))
    if num2<0:
       print("negative number")
       num3=int(input("enter the number"))
       if num3==0:
            print("zero")
       else:
            print ("not zero")
    else:
         print("not negative")  
else:
     print("not positive")        