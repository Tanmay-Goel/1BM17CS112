class admission:
    def __init__(self):
        self.sid=None
        self.marks=None
        self.age=None

    def getter(self):
        return self.sid,self.age,self.marks

    def setter(self,sid,age,marks):
        self.sid=sid
        self.marks=marks
        self.age=age

    def validate_marks(self):
        if(self.marks in range(101)):
            return True
        else:
            return False

    def validate_age(self):
        if(self.age>=20):
            return True
        else:
            return False

    def check_qualification(self):
        if(self.validate_age() and self.validate_marks()):
            if(self.marks>=65):
                return True
            else:
                return False
        else:
            return False
        
a=admission()
b=admission()
print("(Student_id,Age,Marks)")
a.setter(1,20,90)
b.setter(2,19,95)

print(a.getter())
print("Admission: ",a.check_qualification())

print(b.getter())
print("Admission: ",b.check_qualification())

            
