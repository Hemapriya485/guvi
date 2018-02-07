print("Enter the number to check whether it is prime or not:")
num=int(input())
print(num)
count=0
for each_no in range(1,num+1):
    if(num%each_no==0):
        count=count+1
if count==2:
    print("Yes!!!")
else:
    print("No!!!")

