def calc_sum(my_list,K):
    sum=0
    for x in range(K):
        sum=sum+my_list[x]
    return sum
print("Enter the size:")
N=int(input())
print(N)
my_list=[]
for x in range(N):
    my_list.append(int(input()))
print(my_list)
print("Enter K (no.of first K int to be added)")
K=int(input())
sum=calc_sum(my_list,K)
print("sum of first "+str(K)+" integers is "+str(sum))
