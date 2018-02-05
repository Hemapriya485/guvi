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
    vowel_list=['a','e','i','o','u']
    if(user_in.lower() in vowel_list):
        print("It is a vowel")
    else:
        print("It is a consonant")
else:
    print("Please enter a valid alphabet")
