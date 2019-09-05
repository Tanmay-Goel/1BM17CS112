import random
import string

def genpwd(len):
    a=[]
    lc = string.ascii_lowercase
    uc = string.ascii_uppercase
    sc = string.punctuation
    dig = string.digits 
    chars = string.ascii_letters + string.digits + string.punctuation

    a.append(random.choice(lc))
    a.append(random.choice(uc))
    a.append(random.choice(dig))
    a.append(random.choice(sc))         
    a.extend(random.choice(chars) for i in range(len-4))
    random.shuffle(a)
    c=''.join(a)
    return c
             
             
             

n=int(input("Enter length of password (minimum 8): "))
if n>7:
    print(genpwd(n))
else:
    print("invalid length")


                   
