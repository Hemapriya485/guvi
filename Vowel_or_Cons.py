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
