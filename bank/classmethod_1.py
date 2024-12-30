#class method
class student:
    graduation="BE"
    def graduation_in(cls):
        print('graduation',cls.graduation)
student.gra=classmethod(student.graduation_in)
student.gra()
#class method USING DECORATOR
class student:
    graduation="BE"
    @classmethod
    def graduation_in(cls):
        print('graduation',cls.graduation)

student.graduation_in()


#static method
class student:
    @staticmethod
    def rollnumber(y):
        print('roll number',y)
#call
student.rollnumber(101)
