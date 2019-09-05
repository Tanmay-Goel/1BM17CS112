def factors(a):
    b=int(a/2) + 1
    for i in range(1, b):
        if(a%i==0):
            print(i)

n=int(input("Enter number: "))
print("Factors: ")
factors(n)
            
        
    
