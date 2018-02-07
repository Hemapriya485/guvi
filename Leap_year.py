in_year=int(input("Enter the year"))
print(in_year)
if(in_year%4==0):
    if(in_year%100==0):
        if(in_year%400==0):
            print("It is a leap year")
        else:
            print("It is not a leap year")
    else:
        print("It is a leap year")
else:
    print("It is not a leap year")