def revwords(s):
    b=" " 
    l1=s.split(" ")
    l1.reverse()

    b=' '.join(l1)
    print(b)

    l2=s.split(" ")
    a=[]


    for i in l2:
       a.append(i[::-1])

    b=' '.join(a)
    print(b)




s=input("Enter string: ")
revwords(s)
 
