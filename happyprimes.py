def common():
    fp1=open("primenos.txt", "r")
    fp2=open("happynos.txt", "r")
    a=fp1.read()
    a.strip()
    l1=a.split(',')
    b=fp2.read()
    b.strip()
    l2=b.split(',')
    count=0
    for i in l1:
        if i in l2:
            print(i, " ")
            count+=1
            
    fp1.close()
    fp2.close()
    return count

print("Prime numbers that are also happy numbers(upto 1000):\n")
c=common()
print("Count=",c)
