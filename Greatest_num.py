print("Enter three no's:")
num1=int(input("Num1"))
num2=int(input("Num2"))
num3=int(input("Num3"))
print(num1,num2,num3)
if(num1>num2):
    if(num1>num3):
        print("Num1 is greatest!")
    else:
        print("Num3 is greatest!")
elif(num2>num3):
    print("Num2 is greatest!")
