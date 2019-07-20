
# -*- coding:utf -8 -*-
#!/usr/bin/python3

import random

chars = ('+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')

length = input('length for password?')
length = int(length)
good_pass = False

def check_password(p):
    upper = 0
    lower = 0
    number = 0
    symbol = 0

    for i in p:
        if i.isupper():
            upper += 1
   
        elif i.islower():
            lower += 1
   
        elif i.isdigit():
            number += 1
    
        else:
            symbol += 1

    if upper > 0 and lower >0 and number > 0 and symbol >0:
        return True
    else:
        return False

while good_pass != True:
    password =''
    for i in range(length):
        password += random.choice(chars)
    good_pass = check_password(password)
   

print('RESULT:')
print(password)

