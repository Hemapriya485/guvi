num1=int(input("Enter upper range:"))
num2=int(input("Enter lower range:"))
my_list=[]
for x in range(num1+1,num2):
    my_list.append(x)
even_list=list(filter(lambda x:(x%2==0),my_list))
print(*even_list)