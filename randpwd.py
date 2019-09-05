import random
import string

def genpwd(len):
    chars=string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for i in range(len))

n=int(input("Enter length of password (minimum 8): "))
if n>7:
    print(genpwd(n))
else:
    print("invalid length")


                   
