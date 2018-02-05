#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      kalpana
#
# Created:     05/02/2018
# Copyright:   (c) kalpana 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
import string
alpha_letters=[]
alpha_letters=string.ascii_letters
user_in=input()
print(user_in)
if(user_in in alpha_letters):
    print("It is an alphabet")
else:
    print("It is not an alphabet")