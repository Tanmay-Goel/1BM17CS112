class checkstr:
    def __init__(self):
        pass

    def check(self, a):
        stack=[]
        top=-1
        l=len(a)
        sb=['(', '{', '[']
        eb=[')', '}', ']']
        for i in a:
            if i in eb and top==-1:
                return False
            stack.append(i)
            top+=1
            if i in eb:
                b=eb.index(i)
                if sb[b]== stack[top-1]:
                    del(stack[top])
                    del(stack[top-1])
                    top-=2
                else:
                    return False
                
        return True       
                

a=input("Enter string pattern: ")
obj=checkstr()
b=obj.check(a)
if(b==True):
    print("\nValid")
else:
    print("\nInvalid")
            


