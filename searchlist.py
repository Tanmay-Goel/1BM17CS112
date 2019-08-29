def search(a,ele):
    end=n-1
    beg=0
    check=False
    while(beg<=end):
        mid=int((beg+end)/2)
        if(ele==a[mid]):
            return True
        elif(ele>a[mid]):
            beg=mid+1;
        else:
            end=mid-1;
    return False        


a=[]
n=int(input("Enter no. of elements: "))
print("Enter list in ascending order: ")
for i in range(n):
      b=int(input())
      a.append(b)

ele=int(input("Enter search element: "))
print(search(a,ele))


    


      


      
      
