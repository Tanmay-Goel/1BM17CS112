a=[]
b=[]
n=int(input("Enter no. of items: "))
print("\nEnter elements: ")

for i in range(0,n):
    ele=int(input())
    a.append(ele)

for i in a:
    if(i%2==0):
        b.append(i)

print("List with even elements:", b)

    
    
