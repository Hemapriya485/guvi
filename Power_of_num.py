f=lambda num,power:num**power
print("Enter a number and power:")
num=int(input("Number"))
power=int(input("Power"))
print(num,power)
print(str(num)+" raised to the power "+str(power)+" is "+str(f(num,power))+" !!!")
