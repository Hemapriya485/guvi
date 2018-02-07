print("Enter the number:")
a=int(input())
print(a)
n=0
temp1=a
temp2=a
while(temp1>0):
    n=n+1
    temp1=int(temp1/10)
ams=0
while(temp2>0):
    rem=temp2%10
    ams=ams+(rem**n)
    temp2=int(temp2/10)
if(ams==a):
    print("It is an amstrong number!!!")
else:
    print("No,it is not an amstrong number!")
