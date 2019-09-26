class callDetails:
    def __init__(self,c,r,d,t):
        self.clr=c
        self.rcv=r
        self.dur=d
        self.typ=t

    def display(self):
        global count
        print("Caller: ",self.clr)
        print("Reciever: ",self.rcv)
        print("Duration: ",self.dur)
        print("Type: ",self.typ)
        if self.typ=='STD':
            count[0]+=1
        if self.typ=='Local':
            count[1]+=1
        if self.typ=='ISD':
            count[2]+=1
        return count    

class util:
    def __init__(self):
        self.list_of_call_obj=[]
        
    def parse_customer(self,list_of_call_str):
        for i in list_of_call_str:
            x=i.split(",")
            obj=callDetails(*x)
            self.list_of_call_obj.append(obj)
    def disp(self):
        for i in self.list_of_call_obj:
            i.display()
            

call1='9999999999,9000000000,23,STD'
call2='9999999999,9000000001,54,Local'
call3='9999999999,9000000002,6,ISD'

count=[0,0,0]
list_of_call_str=[call1, call2, call3]
obj=util()
obj.parse_customer(list_of_call_str)
obj.disp()

print("\nSTD: %d\nLocal: %d\nISD: %d"%tuple(count))




        
