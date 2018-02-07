def sum_of_natural(n):
    sum=(n*(n+1))/2
    return int(sum)
print("Enter the range:")
n=input()
print(n)
print("Sum of first "+n+" numbers is "+str(sum_of_natural(int(n)))+"!" )