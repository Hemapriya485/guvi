def prime_no(num1,num2):
    prime_list=[]
    for x in range(num1+1,num2):
        n=x
        count=0
        for each_no in range(1,n+1):
            if(n%each_no==0):
                count=count+1
        if count==2:
            prime_list.append(n)
    return prime_list
print("Enter the range:")
num1=int(input())
num2=int(input())
print(num1,num2)
List_of_primes=prime_no(num1,num2)
print(List_of_primes)



